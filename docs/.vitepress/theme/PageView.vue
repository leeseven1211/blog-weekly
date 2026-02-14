<template>
  <div class="page-view-info" v-if="pageView !== null">
    <span class="view-item">👁 本文阅读：{{ pageView ?? '--' }} 次</span>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, watch } from 'vue'
import { useRoute } from 'vitepress'
import { canonicalPath } from './path'

const route = useRoute()
const pageView = ref(null)

let debounceTimer = null
let inflight = null // AbortController
const recordedThisSession = new Set()

// Waline 的计数接口：
// POST /api/article  body: { path: string, type: 'time', action: 'inc' }
// GET  /api/article?path[]=...&type[]=time

async function fetchPageView(key) {
  const path = encodeURIComponent(key)
  const res = await fetch(
    `https://waline.leeseven.online/api/article?path[]=${path}&type[]=time`,
    { method: 'GET', signal: inflight?.signal }
  )
  if (!res.ok) return null
  const data = await res.json()
  const v = Array.isArray(data.data) ? data.data?.[0]?.time : data.data?.time
  return typeof v === 'number' ? v : 0
}

async function recordAndFetch(key) {
  // 取消旧请求，避免竞态覆盖
  if (inflight) inflight.abort()
  inflight = new AbortController()

  try {
    // 每个 canonicalPath 在本次会话只 inc 一次，避免路由抖动刷量
    const shouldInc = !recordedThisSession.has(key)

    if (shouldInc) {
      const res = await fetch('https://waline.leeseven.online/api/article', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ path: key, type: 'time', action: 'inc' }),
        signal: inflight.signal,
      })
      if (res.ok) {
        recordedThisSession.add(key)
        const data = await res.json()
        const v = Array.isArray(data.data) ? data.data?.[0]?.time : data.data?.time
        pageView.value = typeof v === 'number' ? v : 0
        return
      }
      // POST 失败则 fallback GET
    }

    const v = await fetchPageView(key)
    if (v !== null) pageView.value = v
  } catch {
    // 忽略（含 AbortError）
  }
}

function scheduleRecord() {
  if (typeof window === 'undefined') return
  const key = canonicalPath(window.location.pathname)

  pageView.value = null
  if (debounceTimer) clearTimeout(debounceTimer)
  debounceTimer = setTimeout(() => recordAndFetch(key), 120)
}

onMounted(() => {
  scheduleRecord()
})

watch(() => route.path, () => {
  scheduleRecord()
})

onUnmounted(() => {
  if (debounceTimer) {
    clearTimeout(debounceTimer)
    debounceTimer = null
  }
  if (inflight) {
    inflight.abort()
    inflight = null
  }
})
</script>

<style>
.page-view-info {
  display: flex;
  align-items: center;
  gap: 8px;
  margin: 16px 0 0;
  padding: 10px 16px;
  background: var(--vp-c-bg-soft);
  border-radius: 8px;
  font-size: 13px;
  color: var(--vp-c-text-2);
  border: 1px solid var(--vp-c-divider);
}
</style>

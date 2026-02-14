<template>
  <div class="page-view-info" v-if="pageView !== null">
    <span class="view-item">👁 本文阅读：{{ pageView ?? '--' }} 次</span>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import { useRoute } from 'vitepress'

const route = useRoute()
const pageView = ref(null)

// Waline 的计数接口：
// POST /api/article  body: { path: string, type: 'time', action: 'inc' }
// GET  /api/article?path[]=...&type[]=time

async function fetchPageView() {
  try {
    const path = encodeURIComponent(route.path)
    const res = await fetch(
      `https://waline.leeseven.online/api/article?path[]=${path}&type[]=time`,
      { method: 'GET' }
    )
    if (!res.ok) return
    const data = await res.json()
    // 返回形态通常是 data: [{ time: number }]
    const v = Array.isArray(data.data) ? data.data?.[0]?.time : data.data?.time
    pageView.value = typeof v === 'number' ? v : 0
  } catch {
    pageView.value = 0
  }
}

// 上报一次浏览并获取最新数量
async function recordAndFetch() {
  try {
    // 统一使用 VitePress 路由路径（不带 .html），避免同一页面出现两种计数
    const path = route.path
    const res = await fetch('https://waline.leeseven.online/api/article', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ path, type: 'time', action: 'inc' })
    })
    if (!res.ok) return
    const data = await res.json()
    const v = Array.isArray(data.data) ? data.data?.[0]?.time : data.data?.time
    pageView.value = typeof v === 'number' ? v : 0
  } catch {
    // 忽略
  }
}

onMounted(() => {
  recordAndFetch()
})

watch(() => route.path, () => {
  pageView.value = null
  recordAndFetch()
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

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

async function fetchPageView() {
  try {
    const path = encodeURIComponent(window.location.pathname)
    const res = await fetch(
      `https://bot.leeseven.online/waline/api/article?path=${path}`,
      { method: 'GET' }
    )
    if (res.ok) {
      const data = await res.json()
      pageView.value = data.data?.['读数'] ?? data.data?.time ?? data.time ?? 0
    }
  } catch {
    pageView.value = 0
  }
}

// 上报浏览并获取数量
async function recordAndFetch() {
  try {
    const path = window.location.pathname
    const res = await fetch('https://bot.leeseven.online/waline/api/article', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ path, title: document.title })
    })
    if (res.ok) {
      const data = await res.json()
      pageView.value = data.data?.time ?? data.time ?? 1
    }
  } catch {
    pageView.value = null
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

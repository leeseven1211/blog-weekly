<template>
  <div class="waline-wrapper">
    <div class="comment-divider">
      <span>评论 & 点赞</span>
    </div>
    <div id="waline-container"></div>
  </div>
</template>

<script setup>
import { onMounted, onUnmounted, watch } from 'vue'
import { useRoute } from 'vitepress'

const route = useRoute()
let walineInstance = null

async function initWaline() {
  if (typeof window === 'undefined') return
  const { init } = await import('https://unpkg.com/@waline/client@v3/dist/waline.js')
  if (walineInstance) {
    walineInstance.destroy()
  }
  walineInstance = init({
    el: '#waline-container',
    serverURL: 'https://bot.leeseven.online/waline',
    path: window.location.pathname,
    lang: 'zh-CN',
    dark: 'auto',
    reaction: true,
    reactionText: ['点赞', '踩', '惊讶', '感动', '有趣', '有用'],
    reactionTitle: '本文评价',
    copyright: false,
    login: 'disable',
    meta: ['nick'],
    requiredMeta: [],
    placeholder: '留下你的想法，无需登录...',
    wordLimit: 500,
    pageSize: 10,
    emoji: ['//unpkg.com/@waline/emojis@1.2.0/weibo'],
  })
}

onMounted(() => {
  initWaline()
})

watch(() => route.path, () => {
  initWaline()
})

onUnmounted(() => {
  if (walineInstance) {
    walineInstance.destroy()
    walineInstance = null
  }
})
</script>

<style>
@import 'https://unpkg.com/@waline/client@v3/dist/waline.css';

.waline-wrapper {
  margin-top: 48px;
}
.comment-divider {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 24px;
  color: var(--vp-c-text-2);
  font-size: 14px;
}
.comment-divider::before,
.comment-divider::after {
  content: '';
  flex: 1;
  height: 1px;
  background: var(--vp-c-divider);
}
/* Waline 暗色适配 */
.dark .wl-btn {
  background-color: var(--vp-c-brand-1);
}
</style>

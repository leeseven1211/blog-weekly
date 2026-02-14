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
import { init } from '@waline/client'
import '@waline/client/waline.css'
import { canonicalPath } from './path'

const route = useRoute()
let walineInstance = null
let lastPathKey = null
let debounceTimer = null

function mountWaline() {
  if (typeof window === 'undefined') return

  const key = canonicalPath(window.location.pathname)
  if (key === lastPathKey && walineInstance) return

  lastPathKey = key

  if (walineInstance) {
    walineInstance.destroy()
    walineInstance = null
  }

  walineInstance = init({
    el: '#waline-container',
    serverURL: 'https://waline.leeseven.online',
    path: key,
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
    // 本地静态资源（docs/public 会被 VitePress 原样拷贝到站点根目录）
    emoji: ['/waline-emojis/weibo'],
  })
}

function scheduleMount() {
  if (debounceTimer) clearTimeout(debounceTimer)
  debounceTimer = setTimeout(mountWaline, 120)
}

onMounted(() => {
  scheduleMount()
})

watch(() => route.path, () => {
  scheduleMount()
})

onUnmounted(() => {
  if (debounceTimer) {
    clearTimeout(debounceTimer)
    debounceTimer = null
  }
  if (walineInstance) {
    walineInstance.destroy()
    walineInstance = null
  }
})
</script>

<style>
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

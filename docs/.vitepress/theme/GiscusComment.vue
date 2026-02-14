<template>
  <div class="giscus-wrapper">
    <div class="giscus-divider">
      <span>评论 & 点赞</span>
    </div>
    <div ref="giscusContainer"></div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import { useRoute } from 'vitepress'

const route = useRoute()
const giscusContainer = ref(null)

function loadGiscus() {
  if (!giscusContainer.value) return
  // 清除旧实例
  giscusContainer.value.innerHTML = ''

  const script = document.createElement('script')
  script.src = 'https://giscus.app/client.js'
  script.setAttribute('data-repo', 'leeseven1211/blog-weekly')
  script.setAttribute('data-repo-id', 'R_kgDORP9uLQ')
  script.setAttribute('data-category', 'General')
  script.setAttribute('data-category-id', 'DIC_kwDORP9uLc4C2ZpD')
  script.setAttribute('data-mapping', 'pathname')
  script.setAttribute('data-strict', '0')
  script.setAttribute('data-reactions-enabled', '1')
  script.setAttribute('data-emit-metadata', '0')
  script.setAttribute('data-input-position', 'top')
  script.setAttribute('data-theme', 'dark_dimmed')
  script.setAttribute('data-lang', 'zh-CN')
  script.setAttribute('data-loading', 'lazy')
  script.crossOrigin = 'anonymous'
  script.async = true

  giscusContainer.value.appendChild(script)
}

onMounted(() => {
  loadGiscus()
})

watch(() => route.path, () => {
  loadGiscus()
})
</script>

<style>
.giscus-wrapper {
  margin-top: 48px;
  padding-top: 24px;
}
.giscus-divider {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 24px;
  color: var(--vp-c-text-2);
  font-size: 14px;
}
.giscus-divider::before,
.giscus-divider::after {
  content: '';
  flex: 1;
  height: 1px;
  background: var(--vp-c-divider);
}
</style>

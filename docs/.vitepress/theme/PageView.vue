<template>
  <div class="page-view-info">
    <span class="view-item">
      👁 本文阅读：<span id="busuanzi_value_page_pv">--</span> 次
    </span>
    <span class="view-sep">·</span>
    <span class="view-item">
      🌐 全站访问：<span id="busuanzi_value_site_pv">--</span> 次
    </span>
  </div>
</template>

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
.view-sep {
  opacity: 0.4;
}
</style>

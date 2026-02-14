import DefaultTheme from 'vitepress/theme'
import { h } from 'vue'
import WalineComment from './WalineComment.vue'
import PageView from './PageView.vue'
import './custom.css'

function refreshBusuanzi() {
  // 移除旧脚本
  const old = document.getElementById('busuanzi-script')
  if (old) old.remove()
  // 重置计数元素
  const pvEls = document.querySelectorAll('#busuanzi_value_page_pv, #busuanzi_value_site_pv')
  pvEls.forEach(el => { el.textContent = '--' })
  // 重新注入脚本
  const script = document.createElement('script')
  script.id = 'busuanzi-script'
  script.async = true
  script.src = `//busuanzi.ibruce.info/busuanzi/2.4/busuanzi.pure.mini.js?t=${Date.now()}`
  document.head.appendChild(script)
}

export default {
  extends: DefaultTheme,
  Layout() {
    return h(DefaultTheme.Layout, null, {
      'doc-after': () => h('div', [
        h(PageView),
        h(WalineComment),
      ]),
    })
  },
  enhanceApp({ app, router }) {
    if (typeof window !== 'undefined') {
      // 首次加载
      setTimeout(refreshBusuanzi, 500)
      // 路由变化时刷新
      router.onAfterRouteChanged = () => {
        setTimeout(refreshBusuanzi, 300)
      }
    }
  },
}

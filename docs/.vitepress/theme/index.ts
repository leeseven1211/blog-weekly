import DefaultTheme from 'vitepress/theme'
import { h, onMounted } from 'vue'
import GiscusComment from './GiscusComment.vue'
import PageView from './PageView.vue'
import './custom.css'

export default {
  extends: DefaultTheme,
  Layout() {
    return h(DefaultTheme.Layout, null, {
      'doc-after': () => h('div', [
        h(PageView),
        h(GiscusComment),
      ]),
    })
  },
  enhanceApp({ app, router }) {
    // 注入不蒜子统计脚本
    if (typeof window !== 'undefined') {
      const script = document.createElement('script')
      script.async = true
      script.src = '//busuanzi.ibruce.info/busuanzi/2.4/busuanzi.pure.mini.js'
      document.head.appendChild(script)
    }
  },
}

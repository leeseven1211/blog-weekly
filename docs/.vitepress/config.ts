import { defineConfig } from 'vitepress'

export default defineConfig({
  title: '小七的周刊',
  description: '每周一期，记录有趣的技术与世界',
  lang: 'zh-CN',
  base: '/',

  appearance: 'auto', // 支持深色模式

  head: [
    ['link', { rel: 'icon', type: 'image/svg+xml', href: '/favicon.svg' }],
  ],

  themeConfig: {
    logo: '/logo.svg',
    siteTitle: '小七的周刊',

    nav: [
      { text: '首页', link: '/' },
      { text: '归档', link: '/archive' },
      { text: '关于', link: '/about' },
    ],

    sidebar: [
      {
        text: '期数列表',
        items: [
          { text: '第 001 期 - Software 3.0，代码的终结与重生', link: '/issues/issue-001' },
        ],
      },
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com' },
    ],

    footer: {
      message: '每周一期，记录有趣的技术与世界',
      copyright: 'Copyright © 2025 小七的周刊',
    },

    search: {
      provider: 'local',
    },

    darkModeSwitchLabel: '主题',
    lightModeSwitchTitle: '切换到浅色模式',
    darkModeSwitchTitle: '切换到深色模式',
    sidebarMenuLabel: '菜单',
    returnToTopLabel: '返回顶部',
    docFooter: {
      prev: '上一期',
      next: '下一期',
    },
    outline: {
      label: '本页目录',
    },
    lastUpdated: {
      text: '最后更新',
    },
  },
})

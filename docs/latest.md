---
head:
  - - meta
    - property: og:title
      content: 小七的周刊（最新一期）
  - - meta
    - property: og:description
      content: 自动跳转到小七的周刊最新一期。
  - - meta
    - property: og:image
      content: https://blog.leeseven.com/images/issues/013/cover-ai-infra-editorial-v5.jpg
  - - meta
    - property: og:image:secure_url
      content: https://blog.leeseven.com/images/issues/013/cover-ai-infra-editorial-v5.jpg
  - - meta
    - property: og:image:type
      content: image/jpeg
  - - meta
    - property: og:image:width
      content: '2048'
  - - meta
    - property: og:image:height
      content: '1152'
  - - meta
    - property: og:image:alt
      content: 小七的周刊最新一期封面图
  - - meta
    - name: twitter:image
      content: https://blog.leeseven.com/images/issues/013/cover-ai-infra-editorial-v5.jpg
  - - meta
    - itemprop: image
      content: https://blog.leeseven.com/images/issues/013/cover-ai-infra-editorial-v5.jpg
  - - meta
    - property: og:url
      content: https://blog.leeseven.com/latest
---

# 正在跳转到最新一期…

<script setup>
import { onMounted } from 'vue'

onMounted(async () => {
  try {
    const res = await fetch('/feed.xml', { cache: 'no-store' })
    const xml = await res.text()
    const doc = new DOMParser().parseFromString(xml, 'application/xml')

    // 优先取 Atom <entry><link href="...">
    const atomLink = doc.querySelector('entry > link[href]')?.getAttribute('href')
    if (atomLink) {
      location.replace(atomLink)
      return
    }

    // 兼容 RSS <item><link>...</link>
    const rssLink = doc.querySelector('item > link')?.textContent?.trim()
    if (rssLink) {
      location.replace(rssLink)
      return
    }
  } catch (e) {
    // ignore
  }

  // 兜底：跳归档
  location.replace('/archive')
})
</script>

如果没有自动跳转，请点这里：[/archive](/archive)

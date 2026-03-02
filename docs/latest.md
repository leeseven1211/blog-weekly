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

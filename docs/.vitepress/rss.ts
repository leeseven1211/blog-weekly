/**
 * RSS Feed 生成器
 * 在 VitePress buildEnd 钩子中调用，自动扫描 docs/issues/ 下的期刊文件，
 * 生成符合 RSS 2.0 规范的 feed.xml。
 *
 * 零外部依赖——纯字符串拼接，轻量可靠。
 */

import { readFileSync, readdirSync, writeFileSync } from 'node:fs'
import { resolve, join } from 'node:path'

/** 站点元信息 */
const SITE = {
  title: '小七的周刊',
  description: '每周一期，记录有趣的技术与世界。AI · 开源工具 · 科技动态。',
  link: 'https://blog.leeseven.online',
  language: 'zh-CN',
  author: '小七 (OpenClaw Agent)',
  feedUrl: 'https://blog.leeseven.online/feed.xml',
}

/**
 * 从 markdown frontmatter + 内容中提取期刊元信息
 *
 * 日期提取优先级：
 * 1. 正文中的 *YYYY-MM-DD* 格式（斜体日期，通常在"最新一期"引用中）
 * 2. 正文中 "每周一发布" 前后的日期上下文
 * 3. frontmatter og:url 中的期号 → 用归档页面交叉验证
 */
function parseIssue(filePath: string, archiveDates: Record<string, string>) {
  const raw = readFileSync(filePath, 'utf-8')
  const fileName = filePath.split('/').pop()!.replace('.md', '')

  // 提取 frontmatter 中的 date / og:title / og:description
  const fmDate = raw.match(/^date:\s*(\d{4}-\d{2}-\d{2})\s*$/m)?.[1]?.trim()
  const ogTitle = raw.match(/og:title\s*\n\s*content:\s*(.+)/)?.[1]?.trim()
  const ogDesc = raw.match(/og:description\s*\n\s*content:\s*(.+)/)?.[1]?.trim()

  // 提取 H1 标题作为备用
  const h1 = raw.match(/^#\s+(.+)$/m)?.[1]?.trim()

  // 日期：优先读每篇 issue frontmatter；其次从归档页面提取
  const dateStr = fmDate || archiveDates[fileName]
  if (!dateStr) {
    throw new Error(
      `[RSS] 缺少发布日期：${fileName}.md。请在 frontmatter 添加 \'date: YYYY-MM-DD\' 或在 archive.md 中补齐日期。`
    )
  }

  const title = ogTitle || h1 || fileName
  const description = ogDesc || ''

  return {
    title,
    description,
    link: `${SITE.link}/issues/${fileName}.html`,
    pubDate: new Date(dateStr + 'T07:00:00+08:00').toUTCString(),
    guid: `${SITE.link}/issues/${fileName}`,
  }
}

/**
 * 从归档页面（archive.md）解析期号 → 日期的映射
 * 格式示例：- [第 002 期 - ...](/issues/issue-002)（2026-02-15）
 */
function parseArchiveDates(): Record<string, string> {
  const archivePath = resolve(__dirname, '../archive.md')
  const dates: Record<string, string> = {}

  try {
    const content = readFileSync(archivePath, 'utf-8')
    // 匹配 /issues/issue-NNN)（YYYY-MM-DD）
    const regex = /\/issues\/(issue-\d+)\).*?(\d{4}-\d{2}-\d{2})/g
    let match
    while ((match = regex.exec(content)) !== null) {
      dates[match[1]] = match[2]
    }
  } catch {
    // archive.md 不存在也没关系，用默认日期
  }

  return dates
}

/** XML 特殊字符转义 */
function escapeXml(str: string): string {
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&apos;')
}

/** 生成 RSS XML，写入构建输出目录 */
export function generateRss(outDir: string) {
  const issuesDir = resolve(__dirname, '../issues')
  const archiveDates = parseArchiveDates()

  const files = readdirSync(issuesDir)
    .filter(f => f.startsWith('issue-') && f.endsWith('.md'))
    .sort()
    .reverse() // 最新的在前

  const items = files.map(f => {
    const info = parseIssue(join(issuesDir, f), archiveDates)
    return `    <item>
      <title>${escapeXml(info.title)}</title>
      <link>${escapeXml(info.link)}</link>
      <guid isPermaLink="true">${escapeXml(info.guid)}</guid>
      <description>${escapeXml(info.description)}</description>
      <pubDate>${escapeXml(info.pubDate)}</pubDate>
      <author>${escapeXml(SITE.author)}</author>
    </item>`
  })

  const rss = `<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>${escapeXml(SITE.title)}</title>
    <link>${SITE.link}</link>
    <description>${escapeXml(SITE.description)}</description>
    <language>${SITE.language}</language>
    <lastBuildDate>${new Date().toUTCString()}</lastBuildDate>
    <atom:link href="${SITE.feedUrl}" rel="self" type="application/rss+xml"/>
    <image>
      <url>${SITE.link}/favicon.svg</url>
      <title>${escapeXml(SITE.title)}</title>
      <link>${SITE.link}</link>
    </image>
${items.join('\n')}
  </channel>
</rss>
`

  const outputPath = resolve(outDir, 'feed.xml')
  writeFileSync(outputPath, rss, 'utf-8')
  console.log(`✅ RSS feed 已生成: ${outputPath} (${files.length} 篇文章)`)
}

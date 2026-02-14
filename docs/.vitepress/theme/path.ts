// Canonicalize a VitePress route path / window.location.pathname for
// comments + page view counter keys.
//
// Goals:
// - Normalize .html suffix
// - Normalize trailing slash
// - Normalize /index -> /
// - Keep root as '/'

export function canonicalPath(input: string): string {
  if (!input) return '/'

  // Ensure it starts with '/'
  let p = input.startsWith('/') ? input : `/${input}`

  // Drop any accidental query/hash (shouldn't exist on pathname, but safe)
  p = p.split('#')[0].split('?')[0]

  // Decode once (ignore invalid sequences)
  try {
    p = decodeURIComponent(p)
  } catch {
    // ignore
  }

  // Remove .html
  p = p.replace(/\.html$/i, '')

  // Normalize /index
  if (p === '/index') p = '/'

  // Normalize trailing slash (except root)
  if (p.length > 1 && p.endsWith('/')) {
    p = p.slice(0, -1)
  }

  return p || '/'
}

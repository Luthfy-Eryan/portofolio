const BASE_URL = import.meta.env.VITE_API_BASE_URL || '/api'

function formatError(detail) {
  if (!detail) return 'Terjadi kesalahan. Coba lagi sebentar lagi.'
  if (typeof detail === 'string') return detail
  if (Array.isArray(detail)) {
    return detail
      .map((item) => item.msg || item.message || 'Data tidak valid.')
      .join(' ')
  }
  return 'Terjadi kesalahan. Coba lagi sebentar lagi.'
}

async function request(path, options = {}) {
  const response = await fetch(`${BASE_URL}${path}`, {
    headers: { 'Content-Type': 'application/json', ...(options.headers || {}) },
    ...options,
  })

  if (!response.ok) {
    let detail
    try {
      const body = await response.json()
      detail = body.detail
    } catch {
      detail = null
    }
    const error = new Error(formatError(detail))
    error.status = response.status
    throw error
  }

  if (response.status === 204) return null
  return response.json()
}

export const api = {
  getProfile() {
    return request('/profile')
  },
  getSkills() {
    return request('/skills')
  },
  getProjects(params = {}) {
    const query = new URLSearchParams()
    if (params.tag) query.set('tag', params.tag)
    if (params.featured != null) query.set('featured', String(params.featured))
    const suffix = query.toString() ? `?${query.toString()}` : ''
    return request(`/projects${suffix}`)
  },
  getProject(slug) {
    return request(`/projects/${encodeURIComponent(slug)}`)
  },
  getExperiences() {
    return request('/experiences')
  },
  sendContact(payload) {
    return request('/contact', {
      method: 'POST',
      body: JSON.stringify(payload),
    })
  },
}

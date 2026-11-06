const prefersReducedMotion = () =>
  typeof window !== 'undefined' &&
  window.matchMedia('(prefers-reduced-motion: reduce)').matches

let observer

function getObserver() {
  if (!observer) {
    observer = new IntersectionObserver(
      (entries) => {
        for (const entry of entries) {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible')
            observer.unobserve(entry.target)
          }
        }
      },
      { threshold: 0.12, rootMargin: '0px 0px -48px 0px' },
    )
  }
  return observer
}

export default {
  mounted(el, binding) {
    if (prefersReducedMotion()) {
      el.classList.add('reveal', 'is-visible')
      return
    }

    el.classList.add('reveal')
    const delay = Number(binding.value)
    if (delay > 0) el.style.transitionDelay = `${delay}ms`
    getObserver().observe(el)
  },
  unmounted(el) {
    if (observer) observer.unobserve(el)
  },
}

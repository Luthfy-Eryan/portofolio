<script setup>
import { onMounted, onUnmounted, ref } from 'vue'

const open = ref(false)
const scrolled = ref(false)

const items = [
  { label: 'Tentang', hash: '#tentang' },
  { label: 'Keahlian', hash: '#keahlian' },
  { label: 'Proyek', hash: '#proyek' },
  { label: 'Pengalaman', hash: '#pengalaman' },
  { label: 'Kontak', hash: '#kontak' },
]

function handleScroll() {
  scrolled.value = window.scrollY > 16
}

function closeMenu() {
  open.value = false
}

onMounted(() => {
  handleScroll()
  window.addEventListener('scroll', handleScroll, { passive: true })
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>

<template>
  <header class="nav" :class="{ 'nav--scrolled': scrolled }">
    <div class="container nav__inner">
      <RouterLink to="/" class="nav__brand" aria-label="Kembali ke beranda" @click="closeMenu">
        <span class="nav__logo">NK</span>
        <span class="nav__name">Nama Kamu</span>
      </RouterLink>

      <nav class="nav__links" :class="{ 'is-open': open }" aria-label="Navigasi utama">
        <RouterLink
          v-for="item in items"
          :key="item.hash"
          :to="{ path: '/', hash: item.hash }"
          @click="closeMenu"
        >
          {{ item.label }}
        </RouterLink>
        <RouterLink
          class="btn btn--primary nav__cta"
          :to="{ path: '/', hash: '#kontak' }"
          @click="closeMenu"
        >
          Ayo Ngobrol
        </RouterLink>
      </nav>

      <button
        class="nav__toggle"
        :class="{ 'is-open': open }"
        :aria-expanded="open"
        aria-label="Buka menu navigasi"
        @click="open = !open"
      >
        <span></span>
        <span></span>
        <span></span>
      </button>
    </div>
  </header>
</template>

<style scoped>
.nav {
  position: fixed;
  inset: 0 0 auto;
  z-index: 50;
  border-bottom: 1px solid transparent;
  transition:
    background 0.3s var(--ease),
    border-color 0.3s var(--ease),
    backdrop-filter 0.3s var(--ease);
}

.nav--scrolled {
  background: rgba(10, 10, 15, 0.78);
  border-bottom-color: var(--border);
  backdrop-filter: blur(16px);
}

.nav__inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: var(--nav-h);
}

.nav__brand {
  display: inline-flex;
  align-items: center;
  gap: 0.65rem;
  font-weight: 700;
}

.nav__logo {
  display: grid;
  place-items: center;
  width: 38px;
  height: 38px;
  font-size: 0.8rem;
  letter-spacing: 0.05em;
  color: #fff;
  background: var(--gradient);
  border-radius: 12px;
  box-shadow: 0 8px 22px -10px rgba(124, 58, 237, 0.9);
}

.nav__name {
  font-size: 1rem;
  letter-spacing: -0.01em;
}

.nav__links {
  display: flex;
  align-items: center;
  gap: 1.75rem;
}

.nav__links > a:not(.btn) {
  position: relative;
  font-size: 0.92rem;
  color: var(--muted);
  transition: color 0.25s var(--ease);
}

.nav__links > a:not(.btn)::after {
  content: '';
  position: absolute;
  inset: auto 0 -6px;
  height: 2px;
  background: var(--gradient);
  border-radius: 999px;
  transform: scaleX(0);
  transform-origin: left;
  transition: transform 0.28s var(--ease);
}

.nav__links > a:not(.btn):hover {
  color: var(--text);
}

.nav__links > a:not(.btn):hover::after {
  transform: scaleX(1);
}

.nav__cta {
  padding: 0.62rem 1.15rem;
  font-size: 0.88rem;
}

.nav__toggle {
  display: none;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 5px;
  width: 44px;
  height: 44px;
  border: 1px solid var(--border-strong);
  border-radius: 12px;
  cursor: pointer;
}

.nav__toggle span {
  display: block;
  width: 18px;
  height: 2px;
  background: var(--text);
  border-radius: 2px;
  transition:
    transform 0.3s var(--ease),
    opacity 0.3s var(--ease);
}

.nav__toggle.is-open span:nth-child(1) {
  transform: translateY(7px) rotate(45deg);
}

.nav__toggle.is-open span:nth-child(2) {
  opacity: 0;
}

.nav__toggle.is-open span:nth-child(3) {
  transform: translateY(-7px) rotate(-45deg);
}

@media (max-width: 880px) {
  .nav__toggle {
    display: flex;
  }

  .nav__links {
    position: absolute;
    top: calc(var(--nav-h) + 8px);
    right: 1.25rem;
    left: 1.25rem;
    flex-direction: column;
    align-items: stretch;
    gap: 0.35rem;
    padding: 1rem;
    background: rgba(16, 16, 24, 0.97);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    box-shadow: var(--shadow);
    backdrop-filter: blur(18px);
    opacity: 0;
    visibility: hidden;
    transform: translateY(-10px);
    transition:
      opacity 0.28s var(--ease),
      transform 0.28s var(--ease),
      visibility 0.28s var(--ease);
  }

  .nav__links.is-open {
    opacity: 1;
    visibility: visible;
    transform: translateY(0);
  }

  .nav__links > a:not(.btn) {
    padding: 0.7rem 0.85rem;
    border-radius: 10px;
  }

  .nav__links > a:not(.btn):hover {
    background: rgba(255, 255, 255, 0.04);
  }

  .nav__links > a:not(.btn)::after {
    display: none;
  }

  .nav__cta {
    margin-top: 0.4rem;
    justify-content: center;
  }
}
</style>

<script setup>
import { ref, watch } from 'vue'
import { useRoute } from 'vue-router'

import { api } from '../api/client'

const route = useRoute()

const project = ref(null)
const loading = ref(true)
const error = ref('')

async function load(slug) {
  loading.value = true
  error.value = ''
  project.value = null

  try {
    project.value = await api.getProject(slug)
    document.title = `${project.value.title} — Luthfy Eryan Wisesa`
  } catch (err) {
    error.value =
      err.status === 404
        ? 'Proyek tidak ditemukan atau sudah dipindahkan.'
        : err.message
    document.title = 'Proyek tidak ditemukan — Luthfy Eryan Wisesa'
  } finally {
    loading.value = false
  }
}

watch(
  () => route.params.slug,
  (slug) => {
    if (slug) load(slug)
  },
  { immediate: true },
)
</script>

<template>
  <div class="project-detail">
    <div class="container">
      <RouterLink class="project-detail__back" to="/">
        <span aria-hidden="true">←</span> Kembali ke beranda
      </RouterLink>

      <div v-if="loading" class="project-detail__loading" aria-busy="true">
        <div class="skeleton skeleton--title"></div>
        <div class="skeleton skeleton--block"></div>
      </div>

      <div v-else-if="error" class="project-detail__error card" role="alert">
        <h1>{{ error }}</h1>
        <RouterLink class="btn btn--primary" to="/">Kembali ke Beranda</RouterLink>
      </div>

      <article v-else-if="project" class="project-detail__article">
        <header class="project-detail__header" v-reveal>
          <span class="project-detail__year">{{ project.year }}</span>
          <h1>{{ project.title }}</h1>
          <p class="project-detail__summary">{{ project.summary }}</p>

          <ul class="project-detail__tags">
            <li v-for="tag in project.tags" :key="tag" class="tag">{{ tag }}</li>
          </ul>

          <div class="project-detail__actions">
            <a
              v-if="project.demo_url && project.demo_url !== '#'"
              class="btn btn--primary"
              :href="project.demo_url"
              target="_blank"
              rel="noopener noreferrer"
            >
              Lihat Demo ↗
            </a>
            <a
              v-if="project.repo_url && project.repo_url !== '#'"
              class="btn btn--ghost"
              :href="project.repo_url"
              target="_blank"
              rel="noopener noreferrer"
            >
              Lihat Kode ↗
            </a>
          </div>
        </header>

        <div class="project-detail__cover" v-reveal="80">
          <img :src="project.image" :alt="`Pratinjau ${project.title}`" />
        </div>

        <div class="project-detail__body" v-reveal="120">
          <h2>Tentang Proyek</h2>
          <p>{{ project.description }}</p>
        </div>
      </article>
    </div>
  </div>
</template>

<style scoped>
.project-detail {
  padding-top: calc(var(--nav-h) + clamp(2rem, 5vw, 3.5rem));
  padding-bottom: clamp(3rem, 7vw, 6rem);
}

.project-detail__back {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  font-size: 0.88rem;
  font-weight: 500;
  color: var(--muted);
  transition: color 0.25s var(--ease);
}

.project-detail__back:hover {
  color: var(--accent-2);
}

.project-detail__header {
  max-width: 720px;
  margin-top: 1.8rem;
}

.project-detail__year {
  font-size: 0.8rem;
  font-weight: 600;
  letter-spacing: 0.1em;
  color: var(--accent-2);
}

.project-detail__header h1 {
  margin-top: 0.5rem;
  font-size: clamp(2rem, 5vw, 3.2rem);
}

.project-detail__summary {
  margin-top: 1rem;
  font-size: 1.08rem;
  color: var(--muted);
}

.project-detail__tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-top: 1.3rem;
}

.project-detail__actions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.8rem;
  margin-top: 1.8rem;
}

.project-detail__cover {
  margin-top: 2.5rem;
  overflow: hidden;
  border: 1px solid var(--border);
  border-radius: var(--radius);
  background: var(--surface);
}

.project-detail__cover img {
  width: 100%;
  aspect-ratio: 16 / 9;
  object-fit: cover;
}

.project-detail__body {
  max-width: 720px;
  margin-top: 2.5rem;
}

.project-detail__body h2 {
  font-size: 1.4rem;
}

.project-detail__body p {
  margin-top: 0.9rem;
  color: var(--muted);
  white-space: pre-line;
}

.project-detail__loading {
  display: grid;
  gap: 1.2rem;
  margin-top: 2rem;
}

.skeleton {
  background: linear-gradient(
    90deg,
    var(--surface) 25%,
    var(--surface-2) 37%,
    var(--surface) 63%
  );
  background-size: 400% 100%;
  border-radius: var(--radius-sm);
  animation: shimmer 1.4s ease infinite;
}

.skeleton--title {
  width: min(460px, 80%);
  height: 54px;
}

.skeleton--block {
  width: 100%;
  height: 340px;
  border-radius: var(--radius);
}

@keyframes shimmer {
  0% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0 50%;
  }
}

.project-detail__error {
  max-width: 520px;
  margin-top: 2rem;
  padding: 2.5rem;
  text-align: center;
}

.project-detail__error h1 {
  font-size: 1.3rem;
  color: var(--muted);
}

.project-detail__error .btn {
  margin-top: 1.5rem;
}
</style>

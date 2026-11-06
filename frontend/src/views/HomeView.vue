<script setup>
import { computed, onMounted, reactive } from 'vue'

import About from '../components/About.vue'
import Contact from '../components/Contact.vue'
import Experience from '../components/Experience.vue'
import Hero from '../components/Hero.vue'
import Projects from '../components/Projects.vue'
import Skills from '../components/Skills.vue'
import { api } from '../api/client'

const state = reactive({
  profile: null,
  skills: [],
  projects: [],
  experiences: [],
  loading: true,
  error: '',
})

const stats = computed(() => [
  { label: 'Tahun pengalaman', value: '3+' },
  { label: 'Proyek dibangun', value: String(state.projects.length) },
  { label: 'Teknologi dikuasai', value: String(state.skills.length) },
])

async function load() {
  state.loading = true
  state.error = ''

  try {
    const [profile, skills, projects, experiences] = await Promise.all([
      api.getProfile(),
      api.getSkills(),
      api.getProjects(),
      api.getExperiences(),
    ])
    Object.assign(state, { profile, skills, projects, experiences })
  } catch (error) {
    state.error = error.message
  } finally {
    state.loading = false
  }
}

onMounted(load)
</script>

<template>
  <div class="home">
    <div v-if="state.loading" class="container home__loading" aria-busy="true">
      <div class="skeleton skeleton--title"></div>
      <div class="skeleton skeleton--line"></div>
      <div class="skeleton skeleton--line skeleton--short"></div>
      <div class="skeleton skeleton--block"></div>
    </div>

    <div v-else-if="state.error" class="container home__error card" role="alert">
      <h1>Gagal memuat data</h1>
      <p>{{ state.error }}</p>
      <p class="home__error-hint">
        Pastikan backend FastAPI berjalan di
        <code>http://localhost:8000</code>.
      </p>
      <button class="btn btn--primary" type="button" @click="load">Coba Lagi</button>
    </div>

    <template v-else-if="state.profile">
      <Hero :profile="state.profile" />
      <About :profile="state.profile" :stats="stats" />
      <Skills :skills="state.skills" />
      <Projects :projects="state.projects" />
      <Experience :experiences="state.experiences" />
      <Contact :profile="state.profile" />
    </template>
  </div>
</template>

<style scoped>
.home__loading {
  display: grid;
  gap: 1rem;
  padding-top: calc(var(--nav-h) + 4rem);
  padding-bottom: 6rem;
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
  width: min(520px, 90%);
  height: 62px;
}

.skeleton--line {
  width: min(620px, 100%);
  height: 18px;
}

.skeleton--short {
  width: min(420px, 70%);
}

.skeleton--block {
  width: 100%;
  height: 320px;
  margin-top: 1.5rem;
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

.home__error {
  max-width: 560px;
  margin: calc(var(--nav-h) + 5rem) auto;
  padding: 2.5rem;
  text-align: center;
}

.home__error h1 {
  font-size: 1.6rem;
}

.home__error p {
  margin-top: 0.7rem;
  color: var(--muted);
}

.home__error-hint {
  font-size: 0.85rem;
}

.home__error code {
  padding: 0.15rem 0.4rem;
  font-size: 0.82rem;
  color: var(--accent-2);
  background: var(--surface-2);
  border-radius: 6px;
}

.home__error .btn {
  margin-top: 1.5rem;
}
</style>

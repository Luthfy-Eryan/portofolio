<script setup>
import { computed, ref } from 'vue'

import ProjectCard from './ProjectCard.vue'

const props = defineProps({
  projects: {
    type: Array,
    default: () => [],
  },
})

const activeTag = ref('Semua')

const tags = computed(() => [
  'Semua',
  ...new Set(props.projects.flatMap((project) => project.tags)),
])

const filtered = computed(() =>
  activeTag.value === 'Semua'
    ? props.projects
    : props.projects.filter((project) => project.tags.includes(activeTag.value)),
)
</script>

<template>
  <section id="proyek" class="section projects">
    <div class="container">
      <div class="projects__head">
        <div class="section-head" v-reveal>
          <span class="eyebrow">Proyek</span>
          <h2 class="section-title">
            Karya yang pernah
            <span class="gradient-text">saya bangun</span>
          </h2>
          <p class="section-sub">
            Sebagian proyek pilihan yang menunjukkan cara saya merancang,
            membangun, dan menyelesaikan masalah.
          </p>
        </div>

        <div class="projects__filters" v-reveal="80">
          <button
            v-for="tag in tags"
            :key="tag"
            type="button"
            class="projects__filter"
            :class="{ 'is-active': activeTag === tag }"
            @click="activeTag = tag"
          >
            {{ tag }}
          </button>
        </div>
      </div>

      <TransitionGroup name="project-list" tag="div" class="projects__grid">
        <ProjectCard
          v-for="project in filtered"
          :key="project.slug"
          :project="project"
        />
      </TransitionGroup>

      <p v-if="filtered.length === 0" class="projects__empty">
        Belum ada proyek dengan kategori ini.
      </p>
    </div>
  </section>
</template>

<style scoped>
.projects__head {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  gap: 2rem;
  margin-bottom: clamp(2rem, 4vw, 3rem);
}

.projects__head .section-head {
  margin-bottom: 0;
}

.projects__filters {
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-end;
  gap: 0.5rem;
}

.projects__filter {
  padding: 0.45rem 0.95rem;
  font-size: 0.82rem;
  font-weight: 500;
  color: var(--muted);
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 999px;
  cursor: pointer;
  transition:
    color 0.25s var(--ease),
    background 0.25s var(--ease),
    border-color 0.25s var(--ease);
}

.projects__filter:hover {
  color: var(--text);
  border-color: var(--border-strong);
}

.projects__filter.is-active {
  color: #fff;
  background: var(--gradient);
  border-color: transparent;
}

.projects__grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.4rem;
}

.projects__empty {
  padding: 2rem;
  text-align: center;
  color: var(--muted);
}

.project-list-enter-active,
.project-list-leave-active {
  transition:
    opacity 0.35s var(--ease),
    transform 0.35s var(--ease);
}

.project-list-enter-from,
.project-list-leave-to {
  opacity: 0;
  transform: translateY(16px);
}

.project-list-leave-active {
  position: absolute;
}

@media (max-width: 900px) {
  .projects__head {
    flex-direction: column;
    align-items: flex-start;
  }

  .projects__filters {
    justify-content: flex-start;
  }
}

@media (max-width: 720px) {
  .projects__grid {
    grid-template-columns: 1fr;
  }
}
</style>

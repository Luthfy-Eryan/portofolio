<script setup>
defineProps({
  project: {
    type: Object,
    required: true,
  },
})
</script>

<template>
  <article class="project-card card">
    <div class="project-card__media">
      <img :src="project.image" :alt="`Pratinjau ${project.title}`" loading="lazy" />
      <span v-if="project.featured" class="project-card__badge">Unggulan</span>
    </div>

    <div class="project-card__body">
      <span class="project-card__year">{{ project.year }}</span>
      <h3 class="project-card__title">
        <RouterLink :to="{ name: 'project', params: { slug: project.slug } }">
          {{ project.title }}
        </RouterLink>
      </h3>
      <p class="project-card__summary">{{ project.summary }}</p>

      <ul class="project-card__tags">
        <li v-for="tag in project.tags" :key="tag" class="tag">{{ tag }}</li>
      </ul>

      <div class="project-card__actions">
        <RouterLink
          class="project-card__more"
          :to="{ name: 'project', params: { slug: project.slug } }"
        >
          Lihat Detail <span aria-hidden="true">→</span>
        </RouterLink>
        <a
          v-if="project.demo_url && project.demo_url !== '#'"
          :href="project.demo_url"
          target="_blank"
          rel="noopener noreferrer"
        >
          Demo ↗
        </a>
        <a
          v-if="project.repo_url && project.repo_url !== '#'"
          :href="project.repo_url"
          target="_blank"
          rel="noopener noreferrer"
        >
          Kode ↗
        </a>
      </div>
    </div>
  </article>
</template>

<style scoped>
.project-card {
  display: flex;
  flex-direction: column;
  overflow: hidden;
  transition:
    transform 0.35s var(--ease),
    border-color 0.35s var(--ease),
    box-shadow 0.35s var(--ease);
}

.project-card:hover {
  transform: translateY(-6px);
  border-color: var(--border-strong);
  box-shadow: var(--shadow);
}

.project-card__media {
  position: relative;
  aspect-ratio: 16 / 9;
  overflow: hidden;
  background: var(--surface-2);
}

.project-card__media::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, transparent 55%, rgba(10, 10, 15, 0.7));
}

.project-card__media img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.6s var(--ease);
}

.project-card:hover .project-card__media img {
  transform: scale(1.05);
}

.project-card__badge {
  position: absolute;
  top: 0.9rem;
  left: 0.9rem;
  z-index: 1;
  padding: 0.28rem 0.7rem;
  font-size: 0.7rem;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: #fff;
  background: var(--gradient);
  border-radius: 999px;
}

.project-card__body {
  display: flex;
  flex: 1;
  flex-direction: column;
  gap: 0.6rem;
  padding: 1.4rem;
}

.project-card__year {
  font-size: 0.76rem;
  letter-spacing: 0.1em;
  color: var(--muted);
}

.project-card__title {
  font-size: 1.2rem;
}

.project-card__title a {
  transition: color 0.25s var(--ease);
}

.project-card__title a:hover {
  color: var(--accent-2);
}

.project-card__summary {
  font-size: 0.92rem;
  color: var(--muted);
}

.project-card__tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
  margin-top: 0.3rem;
}

.project-card__actions {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 1rem;
  margin-top: auto;
  padding-top: 1.1rem;
  font-size: 0.86rem;
  font-weight: 600;
}

.project-card__more {
  color: var(--accent-2);
}

.project-card__actions a:not(.project-card__more) {
  color: var(--muted);
  transition: color 0.25s var(--ease);
}

.project-card__actions a:not(.project-card__more):hover {
  color: var(--text);
}
</style>

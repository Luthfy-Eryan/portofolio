<script setup>
defineProps({
  profile: {
    type: Object,
    required: true,
  },
  stats: {
    type: Array,
    default: () => [],
  },
})
</script>

<template>
  <section id="tentang" class="section about">
    <div class="container about__grid">
      <div v-reveal>
        <span class="eyebrow">Tentang Saya</span>
        <h2 class="section-title">
          Membangun antarmuka yang
          <span class="gradient-text">enak dipakai</span>
        </h2>
        <p class="about__text">{{ profile.bio }}</p>

        <ul class="about__facts">
          <li>
            <span>Lokasi</span>
            <strong>{{ profile.location }}</strong>
          </li>
          <li>
            <span>Email</span>
            <a :href="`mailto:${profile.email}`">{{ profile.email }}</a>
          </li>
          <li>
            <span>Fokus</span>
            <strong>Vue.js · Python · FastAPI</strong>
          </li>
        </ul>
      </div>

      <div class="about__stats" v-reveal="120">
        <div v-for="stat in stats" :key="stat.label" class="about__stat card">
          <strong>{{ stat.value }}</strong>
          <span>{{ stat.label }}</span>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.about__grid {
  display: grid;
  grid-template-columns: 1.05fr 0.95fr;
  align-items: center;
  gap: clamp(2rem, 6vw, 5rem);
}

.about__text {
  margin-top: 1.3rem;
  color: var(--muted);
}

.about__facts {
  display: grid;
  gap: 0.75rem;
  margin-top: 2rem;
}

.about__facts li {
  display: flex;
  align-items: baseline;
  gap: 1rem;
  padding-bottom: 0.75rem;
  border-bottom: 1px solid var(--border);
  font-size: 0.94rem;
}

.about__facts span {
  min-width: 74px;
  font-size: 0.78rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--muted);
}

.about__facts strong,
.about__facts a {
  font-weight: 600;
  color: var(--text);
}

.about__facts a:hover {
  color: var(--accent-2);
}

.about__stats {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1rem;
}

.about__stat {
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
  padding: 1.6rem;
  transition:
    transform 0.3s var(--ease),
    border-color 0.3s var(--ease);
}

.about__stat:hover {
  transform: translateY(-4px);
  border-color: var(--border-strong);
}

.about__stat strong {
  font-size: clamp(1.9rem, 4vw, 2.6rem);
  line-height: 1;
  background: var(--gradient);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.about__stat span {
  font-size: 0.85rem;
  color: var(--muted);
}

.about__stat:nth-child(1) {
  grid-column: span 2;
}

@media (max-width: 860px) {
  .about__grid {
    grid-template-columns: 1fr;
  }
}
</style>

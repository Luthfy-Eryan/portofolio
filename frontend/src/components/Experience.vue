<script setup>
defineProps({
  experiences: {
    type: Array,
    default: () => [],
  },
})
</script>

<template>
  <section id="pengalaman" class="section experience">
    <div class="container">
      <div class="section-head" v-reveal>
        <span class="eyebrow">Pengalaman</span>
        <h2 class="section-title">
          Perjalanan
          <span class="gradient-text">profesional</span>
        </h2>
        <p class="section-sub">
          Pengalaman yang membentuk cara saya bekerja, berkolaborasi, dan
          menyelesaikan masalah nyata.
        </p>
      </div>

      <ol class="timeline">
        <li
          v-for="(item, index) in experiences"
          :key="item.id"
          class="timeline__item"
          v-reveal="index * 90"
        >
          <span class="timeline__dot" aria-hidden="true"></span>
          <article class="timeline__card card">
            <span class="timeline__period">{{ item.period }}</span>
            <h3 class="timeline__role">{{ item.role }}</h3>
            <span class="timeline__company">{{ item.company }}</span>
            <p class="timeline__desc">{{ item.description }}</p>
          </article>
        </li>
      </ol>
    </div>
  </section>
</template>

<style scoped>
.timeline {
  position: relative;
  display: grid;
  gap: 1.4rem;
  max-width: 780px;
  padding-left: 1.9rem;
}

.timeline::before {
  content: '';
  position: absolute;
  top: 6px;
  bottom: 6px;
  left: 6px;
  width: 2px;
  background: linear-gradient(180deg, var(--accent), var(--accent-2), transparent);
  border-radius: 999px;
  opacity: 0.6;
}

.timeline__item {
  position: relative;
}

.timeline__dot {
  position: absolute;
  top: 1.7rem;
  left: calc(-1.9rem + 1px);
  width: 12px;
  height: 12px;
  background: var(--bg);
  border: 2px solid var(--accent-2);
  border-radius: 50%;
  box-shadow: 0 0 0 4px rgba(34, 211, 238, 0.12);
}

.timeline__card {
  padding: 1.5rem 1.6rem;
  transition:
    transform 0.3s var(--ease),
    border-color 0.3s var(--ease);
}

.timeline__card:hover {
  transform: translateX(4px);
  border-color: var(--border-strong);
}

.timeline__period {
  font-size: 0.76rem;
  font-weight: 600;
  letter-spacing: 0.08em;
  color: var(--accent-2);
}

.timeline__role {
  margin-top: 0.4rem;
  font-size: 1.2rem;
}

.timeline__company {
  display: block;
  margin-top: 0.2rem;
  font-size: 0.9rem;
  font-weight: 500;
  color: var(--text);
}

.timeline__desc {
  margin-top: 0.7rem;
  font-size: 0.92rem;
  color: var(--muted);
}
</style>

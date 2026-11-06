<script setup>
import { computed, onMounted, ref } from 'vue'

const props = defineProps({
  skills: {
    type: Array,
    default: () => [],
  },
})

const ready = ref(false)

onMounted(() => {
  requestAnimationFrame(() => {
    ready.value = true
  })
})

const groups = computed(() => {
  const map = new Map()
  for (const skill of props.skills) {
    if (!map.has(skill.category)) map.set(skill.category, [])
    map.get(skill.category).push(skill)
  }
  return [...map.entries()].map(([name, items]) => ({ name, items }))
})
</script>

<template>
  <section id="keahlian" class="section skills">
    <div class="container">
      <div class="section-head" v-reveal>
        <span class="eyebrow">Keahlian</span>
        <h2 class="section-title">
          Perangkat yang saya
          <span class="gradient-text">kuasai</span>
        </h2>
        <p class="section-sub">
          Kombinasi frontend modern dan backend Python untuk membangun produk
          digital dari ide sampai rilis.
        </p>
      </div>

      <div class="skills__grid">
        <article
          v-for="(group, index) in groups"
          :key="group.name"
          class="skills__group card"
          v-reveal="index * 90"
        >
          <h3 class="skills__group-title">{{ group.name }}</h3>
          <ul class="skills__list">
            <li v-for="skill in group.items" :key="skill.id" class="skills__item">
              <div class="skills__label">
                <span>{{ skill.name }}</span>
                <span class="skills__level">{{ skill.level }}%</span>
              </div>
              <div
                class="skills__track"
                role="progressbar"
                :aria-valuenow="skill.level"
                aria-valuemin="0"
                aria-valuemax="100"
                :aria-label="skill.name"
              >
                <span
                  class="skills__bar"
                  :style="{ width: ready ? `${skill.level}%` : '0%' }"
                ></span>
              </div>
            </li>
          </ul>
        </article>
      </div>
    </div>
  </section>
</template>

<style scoped>
.skills__grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.2rem;
}

.skills__group {
  padding: 1.6rem;
}

.skills__group-title {
  padding-bottom: 0.9rem;
  margin-bottom: 1.2rem;
  font-size: 0.82rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--accent-2);
  border-bottom: 1px solid var(--border);
}

.skills__list {
  display: grid;
  gap: 1.15rem;
}

.skills__label {
  display: flex;
  justify-content: space-between;
  margin-bottom: 0.5rem;
  font-size: 0.92rem;
}

.skills__level {
  font-size: 0.8rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.skills__track {
  height: 6px;
  overflow: hidden;
  background: var(--surface-2);
  border-radius: 999px;
}

.skills__bar {
  display: block;
  height: 100%;
  background: var(--gradient);
  border-radius: 999px;
  transition: width 1.1s var(--ease);
}

@media (max-width: 900px) {
  .skills__grid {
    grid-template-columns: 1fr 1fr;
  }
}

@media (max-width: 620px) {
  .skills__grid {
    grid-template-columns: 1fr;
  }
}
</style>

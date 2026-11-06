<script setup>
defineProps({
  profile: {
    type: Object,
    required: true,
  },
})
</script>

<template>
  <section id="beranda" class="hero">
    <div class="container hero__inner">
      <div class="hero__content">
        <span class="hero__badge" v-reveal>
          <span class="hero__dot"></span>
          Tersedia untuk kolaborasi
        </span>

        <h1 class="hero__title" v-reveal="60">
          Halo, saya
          <span class="gradient-text">{{ profile.name }}</span>
        </h1>

        <p class="hero__headline" v-reveal="120">{{ profile.headline }}</p>
        <p class="hero__bio" v-reveal="160">{{ profile.bio }}</p>

        <div class="hero__actions" v-reveal="200">
          <RouterLink class="btn btn--primary" :to="{ path: '/', hash: '#proyek' }">
            Lihat Proyek
            <span aria-hidden="true">→</span>
          </RouterLink>
          <RouterLink class="btn btn--ghost" :to="{ path: '/', hash: '#kontak' }">
            Hubungi Saya
          </RouterLink>
        </div>

        <ul class="hero__socials" v-reveal="240">
          <li v-for="social in profile.socials" :key="social.label">
            <a :href="social.url" target="_blank" rel="noopener noreferrer">
              {{ social.label }}
              <span aria-hidden="true">↗</span>
            </a>
          </li>
        </ul>
      </div>

      <div class="hero__visual" v-reveal="140">
        <div class="hero__glow" aria-hidden="true"></div>
        <div class="hero__avatar">
          <img :src="profile.avatar" :alt="`Foto ${profile.name}`" />
        </div>
        <span class="hero__chip hero__chip--top">Vue.js</span>
        <span class="hero__chip hero__chip--bottom">Python · FastAPI</span>
      </div>
    </div>

    <div class="container hero__scroll">
      <span class="hero__scroll-line" aria-hidden="true"></span>
      <span>Gulir untuk menjelajah</span>
    </div>
  </section>
</template>

<style scoped>
.hero {
  position: relative;
  padding-top: calc(var(--nav-h) + clamp(3rem, 7vw, 6rem));
  overflow: hidden;
}

.hero__inner {
  display: grid;
  grid-template-columns: 1.15fr 0.85fr;
  align-items: center;
  gap: clamp(2rem, 6vw, 4.5rem);
}

.hero__badge {
  display: inline-flex;
  align-items: center;
  gap: 0.55rem;
  padding: 0.35rem 0.85rem;
  font-size: 0.78rem;
  font-weight: 500;
  color: var(--accent-2);
  background: rgba(34, 211, 238, 0.08);
  border: 1px solid rgba(34, 211, 238, 0.25);
  border-radius: 999px;
}

.hero__dot {
  width: 7px;
  height: 7px;
  background: var(--accent-2);
  border-radius: 50%;
  box-shadow: 0 0 0 0 rgba(34, 211, 238, 0.6);
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0% {
    box-shadow: 0 0 0 0 rgba(34, 211, 238, 0.55);
  }
  70% {
    box-shadow: 0 0 0 8px rgba(34, 211, 238, 0);
  }
  100% {
    box-shadow: 0 0 0 0 rgba(34, 211, 238, 0);
  }
}

.hero__title {
  margin-top: 1.4rem;
  font-size: clamp(2.6rem, 6.5vw, 4.4rem);
  letter-spacing: -0.035em;
}

.hero__headline {
  margin-top: 1rem;
  font-size: clamp(1.05rem, 2vw, 1.3rem);
  font-weight: 500;
  color: var(--text);
}

.hero__bio {
  max-width: 54ch;
  margin-top: 1.1rem;
  color: var(--muted);
}

.hero__actions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.8rem;
  margin-top: 2rem;
}

.hero__socials {
  display: flex;
  flex-wrap: wrap;
  gap: 1.4rem;
  margin-top: 2.2rem;
}

.hero__socials a {
  display: inline-flex;
  align-items: center;
  gap: 0.3rem;
  font-size: 0.86rem;
  font-weight: 500;
  color: var(--muted);
  transition: color 0.25s var(--ease);
}

.hero__socials a:hover {
  color: var(--accent-2);
}

.hero__visual {
  position: relative;
  display: grid;
  place-items: center;
  min-height: 380px;
}

.hero__glow {
  position: absolute;
  width: 340px;
  height: 340px;
  background: var(--gradient);
  filter: blur(90px);
  opacity: 0.35;
  border-radius: 50%;
}

.hero__avatar {
  position: relative;
  width: min(330px, 78vw);
  aspect-ratio: 1;
  padding: 4px;
  background: var(--gradient);
  border-radius: 50%;
  box-shadow: var(--shadow);
  animation: floaty 7s ease-in-out infinite;
}

.hero__avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  background: var(--surface);
  border: 6px solid var(--bg);
  border-radius: 50%;
}

.hero__chip {
  position: absolute;
  padding: 0.5rem 0.95rem;
  font-size: 0.8rem;
  font-weight: 600;
  color: var(--text);
  background: rgba(20, 20, 28, 0.9);
  border: 1px solid var(--border-strong);
  border-radius: 999px;
  box-shadow: var(--shadow);
  backdrop-filter: blur(8px);
}

.hero__chip--top {
  top: 8%;
  right: 2%;
  animation: floaty 6s ease-in-out infinite;
}

.hero__chip--bottom {
  bottom: 8%;
  left: 0;
  animation: floaty 8s ease-in-out 0.6s infinite;
}

@keyframes floaty {
  0%,
  100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-12px);
  }
}

.hero__scroll {
  display: flex;
  align-items: center;
  gap: 0.7rem;
  margin-top: clamp(2.5rem, 6vw, 4.5rem);
  padding-bottom: 2rem;
  font-size: 0.78rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--muted);
}

.hero__scroll-line {
  width: 46px;
  height: 1px;
  background: linear-gradient(90deg, var(--accent-2), transparent);
}

@media (max-width: 900px) {
  .hero__inner {
    grid-template-columns: 1fr;
    text-align: center;
  }

  .hero__bio {
    margin-inline: auto;
  }

  .hero__actions,
  .hero__socials {
    justify-content: center;
  }

  .hero__visual {
    order: -1;
    min-height: 300px;
  }

  .hero__avatar {
    width: min(260px, 68vw);
  }

  .hero__scroll {
    justify-content: center;
  }
}
</style>

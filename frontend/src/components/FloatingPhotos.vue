<script setup>
const photos = [
  {
    src: '/images/foto1.jpg',
    alt: 'Foto 1',
    style: { top: '12%', left: '3%' },
    rotate: '-8deg',
    duration: '9s',
    delay: '0s',
  },
  {
    src: '/images/foto2.jpg',
    alt: 'Foto 2',
    style: { top: '38%', right: '4%' },
    rotate: '6deg',
    duration: '11s',
    delay: '0.8s',
  },
  {
    src: '/images/foto3.jpg',
    alt: 'Foto 3',
    style: { top: '64%', left: '5%' },
    rotate: '5deg',
    duration: '10s',
    delay: '0.4s',
  },
  {
    src: '/images/foto4.jpg',
    alt: 'Foto 4',
    style: { top: '86%', right: '3%' },
    rotate: '-6deg',
    duration: '12s',
    delay: '1.2s',
  },
]

function onImageError(event) {
  const image = event.target
  if (image.dataset.fallback) return
  image.dataset.fallback = 'true'
  image.src = '/images/avatar.svg'
}
</script>

<template>
  <div class="floating-photos" aria-hidden="true">
    <figure
      v-for="(photo, index) in photos"
      :key="photo.src"
      class="floating-photos__slot"
      :style="photo.style"
      v-reveal="index * 90"
    >
      <div
        class="floating-photos__frame"
        :style="{
          '--rotate': photo.rotate,
          '--duration': photo.duration,
          '--delay': photo.delay,
        }"
      >
        <img
          :src="photo.src"
          :alt="photo.alt"
          loading="lazy"
          @error="onImageError"
        />
      </div>
    </figure>
  </div>
</template>

<style scoped>
.floating-photos {
  position: absolute;
  inset: 0;
  z-index: 0;
  overflow: hidden;
  pointer-events: none;
}

.floating-photos__slot {
  position: absolute;
  width: clamp(96px, 12vw, 160px);
}

.floating-photos__frame {
  width: 100%;
  padding: 0.5rem 0.5rem 1.7rem;
  background: var(--surface);
  border: 1px solid var(--border-strong);
  border-radius: 10px;
  box-shadow: var(--shadow);
  opacity: 0.5;
  transform: rotate(var(--rotate));
  animation: float-photo var(--duration) ease-in-out var(--delay) infinite;
  will-change: transform;
}

.floating-photos__frame img {
  width: 100%;
  aspect-ratio: 4 / 5;
  object-fit: cover;
  border-radius: 6px;
  background: var(--surface-2);
}

@keyframes float-photo {
  0%,
  100% {
    transform: rotate(var(--rotate)) translateY(0);
  }
  50% {
    transform: rotate(var(--rotate)) translateY(-18px);
  }
}

@media (max-width: 1024px) {
  .floating-photos__slot {
    width: clamp(70px, 10vw, 110px);
  }

  .floating-photos__frame {
    opacity: 0.4;
  }
}

@media (max-width: 640px) {
  .floating-photos__slot {
    width: clamp(56px, 20vw, 80px);
  }

  .floating-photos__frame {
    padding: 0.3rem 0.3rem 1rem;
    opacity: 0.32;
  }
}
</style>

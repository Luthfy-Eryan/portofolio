<script setup>
document.title = 'Halaman tidak ditemukan — Luthfy Eryan Wisesa'
</script>

<template>
  <div class="not-found container">
    <span class="not-found__code">404</span>
    <h1>Halaman tidak ditemukan</h1>
    <p>Sepertinya halaman yang kamu cari sudah berpindah atau tidak pernah ada.</p>
    <RouterLink class="btn btn--primary" to="/">Kembali ke Beranda</RouterLink>
  </div>
</template>

<style scoped>
.not-found {
  display: grid;
  justify-items: center;
  gap: 0.9rem;
  min-height: 78vh;
  padding-top: calc(var(--nav-h) + 4rem);
  text-align: center;
  align-content: center;
}

.not-found__code {
  font-size: clamp(4rem, 14vw, 8rem);
  font-weight: 800;
  line-height: 1;
  background: var(--gradient);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.not-found h1 {
  font-size: clamp(1.4rem, 3vw, 2rem);
}

.not-found p {
  max-width: 42ch;
  color: var(--muted);
}

.not-found .btn {
  margin-top: 0.8rem;
}
</style>

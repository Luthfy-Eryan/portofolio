<template>
  <footer class="footer">
    <div class="container footer__inner">
      <div class="footer__brand">
        <span class="footer__logo">LEW</span>
        <div>
          <strong>Luthfy Eryan Wisesa</strong>
          <p>Full-Stack Developer & UI Enthusiast</p>
        </div>
      </div>

      <p class="footer__copy">
        © Portofolio Luthfy Eryan Wisesa. Dibangun dengan Vue.js & FastAPI.
      </p>

      <a class="footer__top" href="#beranda">Kembali ke atas ↑</a>
    </div>
  </footer>
</template>

<style scoped>
.footer {
  border-top: 1px solid var(--border);
  background: rgba(10, 10, 15, 0.6);
}

.footer__inner {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 1.2rem;
  padding: 2rem 0;
}

.footer__brand {
  display: flex;
  align-items: center;
  gap: 0.7rem;
}

.footer__logo {
  display: grid;
  place-items: center;
  width: 36px;
  height: 36px;
  font-size: 0.76rem;
  letter-spacing: 0.05em;
  color: #fff;
  background: var(--gradient);
  border-radius: 10px;
}

.footer__brand strong {
  font-size: 0.94rem;
}

.footer__brand p {
  font-size: 0.78rem;
  color: var(--muted);
}

.footer__copy {
  font-size: 0.8rem;
  color: var(--muted);
}

.footer__top {
  font-size: 0.8rem;
  font-weight: 600;
  color: var(--accent-2);
}

@media (max-width: 720px) {
  .footer__inner {
    flex-direction: column;
    align-items: flex-start;
  }
}
</style>

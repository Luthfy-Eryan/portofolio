<script setup>
import { reactive } from 'vue'

import { api } from '../api/client'

defineProps({
  profile: {
    type: Object,
    default: null,
  },
})

const form = reactive({
  name: '',
  email: '',
  subject: '',
  message: '',
})

const status = reactive({
  sending: false,
  success: '',
  error: '',
})

async function onSubmit() {
  status.success = ''
  status.error = ''
  status.sending = true

  try {
    const result = await api.sendContact({ ...form })
    status.success = result.message
    form.name = ''
    form.email = ''
    form.subject = ''
    form.message = ''
  } catch (error) {
    status.error = error.message
  } finally {
    status.sending = false
  }
}
</script>

<template>
  <section id="kontak" class="section contact">
    <div class="container contact__grid">
      <div class="contact__intro" v-reveal>
        <span class="eyebrow">Kontak</span>
        <h2 class="section-title">
          Punya ide? Mari
          <span class="gradient-text">bicara</span>
        </h2>
        <p class="section-sub">
          Terbuka untuk proyek freelance, kolaborasi, atau sekadar ngobrol soal
          teknologi. Kirim pesan dan saya akan membalas secepatnya.
        </p>

        <ul v-if="profile" class="contact__info">
          <li>
            <span>Email</span>
            <a :href="`mailto:${profile.email}`">{{ profile.email }}</a>
          </li>
          <li>
            <span>Lokasi</span>
            <strong>{{ profile.location }}</strong>
          </li>
        </ul>

        <ul v-if="profile" class="contact__socials">
          <li v-for="social in profile.socials" :key="social.label">
            <a :href="social.url" target="_blank" rel="noopener noreferrer">
              {{ social.label }} ↗
            </a>
          </li>
        </ul>
      </div>

      <form class="contact__form card" v-reveal="100" @submit.prevent="onSubmit">
        <div class="contact__row">
          <div class="contact__field">
            <label for="contact-name">Nama</label>
            <input
              id="contact-name"
              v-model.trim="form.name"
              type="text"
              name="name"
              placeholder="Nama lengkap"
              autocomplete="name"
              required
              minlength="2"
            />
          </div>
          <div class="contact__field">
            <label for="contact-email">Email</label>
            <input
              id="contact-email"
              v-model.trim="form.email"
              type="email"
              name="email"
              placeholder="kamu@email.com"
              autocomplete="email"
              required
            />
          </div>
        </div>

        <div class="contact__field">
          <label for="contact-subject">Subjek <span>(opsional)</span></label>
          <input
            id="contact-subject"
            v-model.trim="form.subject"
            type="text"
            name="subject"
            placeholder="Tentang apa?"
          />
        </div>

        <div class="contact__field">
          <label for="contact-message">Pesan</label>
          <textarea
            id="contact-message"
            v-model.trim="form.message"
            name="message"
            rows="5"
            placeholder="Ceritakan ide atau kebutuhanmu..."
            required
            minlength="10"
          ></textarea>
        </div>

        <p v-if="status.success" class="contact__alert contact__alert--success" role="status">
          {{ status.success }}
        </p>
        <p v-if="status.error" class="contact__alert contact__alert--error" role="alert">
          {{ status.error }}
        </p>

        <button class="btn btn--primary contact__submit" type="submit" :disabled="status.sending">
          {{ status.sending ? 'Mengirim...' : 'Kirim Pesan' }}
          <span v-if="!status.sending" aria-hidden="true">→</span>
        </button>
      </form>
    </div>
  </section>
</template>

<style scoped>
.contact__grid {
  display: grid;
  grid-template-columns: 0.9fr 1.1fr;
  gap: clamp(2rem, 5vw, 4rem);
  align-items: start;
}

.contact__info {
  display: grid;
  gap: 0.8rem;
  margin-top: 2rem;
}

.contact__info li {
  display: flex;
  gap: 1rem;
  align-items: baseline;
  font-size: 0.94rem;
}

.contact__info span {
  min-width: 64px;
  font-size: 0.76rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--muted);
}

.contact__info a,
.contact__info strong {
  font-weight: 600;
}

.contact__info a:hover {
  color: var(--accent-2);
}

.contact__socials {
  display: flex;
  flex-wrap: wrap;
  gap: 1.2rem;
  margin-top: 1.8rem;
}

.contact__socials a {
  font-size: 0.86rem;
  color: var(--muted);
  transition: color 0.25s var(--ease);
}

.contact__socials a:hover {
  color: var(--accent-2);
}

.contact__form {
  display: grid;
  gap: 1.1rem;
  padding: clamp(1.4rem, 3vw, 2rem);
}

.contact__row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.contact__field {
  display: grid;
  gap: 0.45rem;
}

.contact__field label {
  font-size: 0.82rem;
  font-weight: 600;
  color: var(--text);
}

.contact__field label span {
  font-weight: 400;
  color: var(--muted);
}

.contact__field input,
.contact__field textarea {
  width: 100%;
  padding: 0.75rem 0.9rem;
  font-size: 0.92rem;
  color: var(--text);
  background: var(--bg-soft);
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  outline: none;
  resize: vertical;
  transition:
    border-color 0.25s var(--ease),
    box-shadow 0.25s var(--ease);
}

.contact__field input::placeholder,
.contact__field textarea::placeholder {
  color: #6b7280;
}

.contact__field input:focus,
.contact__field textarea:focus {
  border-color: var(--accent-2);
  box-shadow: 0 0 0 3px rgba(34, 211, 238, 0.15);
}

.contact__alert {
  padding: 0.7rem 0.9rem;
  font-size: 0.86rem;
  border-radius: var(--radius-sm);
}

.contact__alert--success {
  color: #6ee7b7;
  background: rgba(16, 185, 129, 0.1);
  border: 1px solid rgba(16, 185, 129, 0.3);
}

.contact__alert--error {
  color: #fca5a5;
  background: rgba(239, 68, 68, 0.1);
  border: 1px solid rgba(239, 68, 68, 0.3);
}

.contact__submit {
  justify-self: start;
}

@media (max-width: 860px) {
  .contact__grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 520px) {
  .contact__row {
    grid-template-columns: 1fr;
  }

  .contact__submit {
    justify-self: stretch;
  }
}
</style>

import { createApp } from 'vue'

import App from './App.vue'
import router from './router'
import reveal from './directives/reveal'

import './assets/styles/tokens.css'
import './assets/styles/base.css'
import './assets/styles/utilities.css'

createApp(App).use(router).directive('reveal', reveal).mount('#app')

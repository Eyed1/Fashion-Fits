import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import Vueticol from 'vueticol';
import 'vueticol/dist/vueticol.css';

import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(Vueticol);

app.mount('#app')

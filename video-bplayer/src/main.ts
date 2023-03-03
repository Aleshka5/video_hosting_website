import { createApp } from 'vue';
import '@/assets/bootstrap/css/bootstrap.min.css';
import '@/assets/css/osahan.css';
import 'video.js/dist/video-js.css';
import App from './App.vue';
import router from './router';
import store from './store';

createApp(App).use(store).use(router).mount('#app');

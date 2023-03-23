import { createApp } from 'vue';
import '@/assets/bootstrap/css/bootstrap.min.css';
import '@/assets/css/osahan.css';
import '@/assets/css/font.all.min.css';
import utils from '@/services/utils';
import 'video.js/dist/video-js.css';
import App from './App.vue';
import router from './router';
import store from './store';

const app = createApp(App).use(store).use(router);

app.config.globalProperties.$utils = utils;

app.mount('#app');

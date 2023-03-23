import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';
import HomeView from '@/views/HomeView.vue';
import VideoView from '@/views/VideoView.vue';
import UploadView from '@/views/UploadView.vue';
import LoginView from '@/views/LoginView.vue';
import RegisterView from '@/views/RegisterView.vue';
import MainLayout from '@/views/MainLayout.vue';

const routes: Array<RouteRecordRaw> = [
  {
    path: '/login',
    name: 'login',
    component: LoginView,
  },
  {
    path: '/register',
    name: 'register',
    component: RegisterView,
  },
  {
    path: '',
    name: 'main',
    component: MainLayout,
    children: [
      {
        path: '',
        name: 'home',
        component: HomeView,
      },
      {
        path: '/video',
        name: 'video',
        component: HomeView,
      },
      {
        path: '/video/:id',
        name: 'video_id',
        component: VideoView,
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        // component: () => import(/* webpackChunkName: "about" */ '../views/VideoView.vue'),
      },
      {
        path: '/upload',
        name: 'upload',
        component: UploadView,
      },
    ],
  },

];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;

// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import ChatBox from '../components/ChatBox.vue';
import VisualizationTab from '../components/VisualizationTab.vue';

// Define routes
const routes = [
  { path: '/', component: ChatBox },
  { path: '/visualization', component: VisualizationTab },
];

// Initialize and export the router
const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;

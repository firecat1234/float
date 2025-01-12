import { createApp } from 'vue'
import App from './App.vue'
import './style.css' // place holder for styles
import { createRouter, createWebHistory } from 'vue-router'
import ChatBox from './components/ChatBox.vue'
import VisualizationTab from './components/VisualizationTab.vue'

// define routes
const routes = [
  {path: '/', component: ChatBox},
  {path: '/visualization', component: VisualizationTab}
]

// initialize the vue router
const router = createRouter({
    history: createWebHistory(),
    routes
})


createApp(App).use(router).mount('#app')
import { createApp } from 'vue';
import App from './App.vue';
import './style.css'; // Placeholder for styles
import router from './router'; // Import the router

const app = createApp(App);
app.use(router);
app.mount('#app');

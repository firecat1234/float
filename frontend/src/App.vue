<template>
    <div id="app">
       <nav>
         <router-link to="/">Chat</router-link>
         <router-link to="/visualization">Visualization</router-link>
       </nav>
       <router-view />
    </div>
</template>
<style>
  body {
  margin: 0;
  padding: 0;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

nav {
  padding: 1rem;
  display: flex;
  justify-content: center;
  gap: 20px;
}
</style>
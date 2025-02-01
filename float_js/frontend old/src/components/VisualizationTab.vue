<template>
    <div>
        <h1>Visualization Tab</h1>
        <p>This is the visualization tab. A good place to create visualizations!</p>
        <!-- Placeholder for visualizations, for example: -->
        <div id="graph-container">
            <!-- Graph will go here -->
        </div>
    </div>
</template>
<script>
export default {
    mounted() {
        // perform data gathering for visualization here.
        // or just set this up as a placeholder for data exploration.
    }
}
</script>
<style scoped>
#graph-container {
  border: 2px solid black;
  height: 300px;
  width: 600px;
  margin: auto;
}
</style>
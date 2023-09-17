<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <footer>
    <nav>
      <RouterLink id="fits" to="/">Fits</RouterLink>
      <RouterLink id="wardrope" to="/wardrope">Wardrope</RouterLink>
    </nav>
  </footer>

  <RouterView class="view" />
</template>

<style scoped>
footer {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  height: 7vh;
  background-color: rgb(250, 250, 250);
  border-top: 0.1px solid black;
}
.view{
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 93vh;
}
/* remember to style button presses */
#fits {
  color: #000;
  text-decoration: none;
  position: fixed;
  padding: 20px;
  left: 0;
  bottom: 0;
}
#wardrope {
  color: #000;
  text-decoration: none;
  position: fixed;
  padding: 20px;
  right: 0;
  bottom: 0;
}
</style>

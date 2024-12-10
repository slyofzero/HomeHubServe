<script setup lang="ts">
import Header from "./components/Header.vue";
</script>

<template>
  <Header></Header>

  <div class="p-md-4 mt-4 mx-auto max-w"><RouterView></RouterView></div>
</template>

<style scoped>
.max-w {
  max-width: 80%;
}
</style>

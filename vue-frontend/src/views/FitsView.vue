<script setup>
import { ref } from 'vue'
import { useWardropeStore } from '../stores/wardropeStore'

const wardropeStore = useWardropeStore()
const fits = wardropeStore.getFits()


</script>


<template>
  <header>
    <h1>Rizzy Fits</h1>
  </header>
  <main>
    <FitsCard v-for="fit in fits" :key="fit.id" :fit="fit" /> 
  </main>
</template>

<style>
main{
  display: flex;
  flex-wrap: wrap;
  flex-direction: column;
  justify-content: space-evenly;
}

</style>

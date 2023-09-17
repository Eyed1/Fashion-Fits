<script setup>
import { computed, ref } from 'vue'
import { useWardropeStore } from '../stores/wardropeStore'
import ClotheCard from '../components/ClotheCard.vue'
import ClotheEditPopup from '../components/ClotheEditPopup.vue'

const category = ref('top')
const wardropeStore = useWardropeStore()
wardropeStore.getWardrope()
const clothes = computed(() => {
  return wardropeStore.getClothesByCategory(category.value)
})
console.log(clothes.value)
const showPopup = ref(false)
const popupClothe = ref({})

const popupEdit = (clothe) => {
  console.log(clothe)
  showPopup.value = true
  popupClothe.value = clothe
}

const finishEdit = (clothe) => {
  showPopup.value = false
  wardropeStore.updateClothe(clothe)
}

</script>


<template>
  <div>
  <header>
    <nav>
      <div @click="category='top'" class="nav-item">Tops</div>
      <div @click="category='bottom'" class="nav-item">Bottoms</div>
      <div @click="category='outerwear'" class="nav-item">Outerwear</div>
    </nav>
  </header>
  <main>
    <ClotheCard v-for="clothe in clothes.value" :key="clothe.id" :clothe="clothe" @click="popupEdit(clothe)"/> 
  </main>
  <ClotheEditPopup v-if="showPopup" :clothe="popupClothe" @close="finishEdit"/>
  </div>
</template>

<style>
nav{
  display: flex;
  flex-wrap: nowrap;
  justify-content: space-evenly;
}

main{
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: space-evenly;
}

.nav-item{
  padding: 20px;
  cursor: pointer;
}
</style>

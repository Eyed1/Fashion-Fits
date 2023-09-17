<script setup>
import { computed, ref } from 'vue'
import { useWardropeStore } from '../stores/wardropeStore'
import ClotheCard from '../components/ClotheCard.vue'
import ClotheEditPopup from '../components/ClotheEditPopup.vue'
import ClotheCreatePopup from '../components/ClotheCreatePopup.vue';

const category = ref('top')
const wardropeStore = useWardropeStore()
wardropeStore.getWardrope()
const clothes = computed(() => {
  return wardropeStore.getClothesByCategory(category.value)
})
console.log(clothes.value)
const showEdit = ref(false)
const showCreate = ref(false)
const popupClothe = ref({})

const popupEdit = (clothe) => {
  console.log(clothe)
  showEdit.value = true
  popupClothe.value = clothe
}

const finishEdit = (clothe, remove) => {
  showEdit.value = false
  if (remove) {
    wardropeStore.deleteClothe(clothe)
    return
  }
  wardropeStore.updateClothe(clothe)
}

const openCreateClothe = () => {
  showCreate.value = true
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
    <ClotheCard v-for="clothe in clothes.value" :key="clothe.id" :imgLink="clothe.imgLink" :text="`${clothe.type}`" @click="popupEdit(clothe)"/> 
  </main>
  <button id="addButton" @click="openCreateClothe">+</button>
  <ClotheEditPopup v-if="showEdit" :clothe="popupClothe" @close="finishEdit"/>
  <ClotheCreatePopup v-if="showCreate" @close="showCreate=false"/>
  </div>
</template>

<style scoped>
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

#addButton{
  position: fixed;
  bottom: 7vh;
  right: 0;
  transform: translate(-20px, -20px);
  width: 50px;
  height: 50px;
  border-radius: 50%;
  border: none;
  font-size: 30px;
  font-weight: bold;
  cursor: pointer;
  background-color: rgb(150, 255, 150);
  color: green;
}
#addButton:hover{
  background-color: rgb(100, 255, 100);
}
</style>

import { ref, computed } from 'vue'
import { WardropeService } from '../services/wardropeService'
import { defineStore } from 'pinia'

export const useWardropeStore = defineStore('wardrope', () => {
  const wardrope = ref([])
  const fits = ref([])
  const wardropeService = new WardropeService()

  async function getWardrope() {
    wardrope.value = await wardropeService.getWardrope()
    return wardrope.value
  }

  function getClothesByCategory(category) {
    return computed(() => wardrope.value.filter(clothe => clothe.category === category))
  }

  async function getFits() {
    fits.value = await wardropeService.getFits()
    return fits.value
  }

  async function addClothe(clothe) {
    wardrope.value = await wardropeService.addClothe(clothe)
  }

  async function removeClothe(clothe) {
    wardrope.value = await wardropeService.removeClothe(clothe)
  }

  async function editClothe(clothe) {
    wardrope.value = await wardropeService.editClothe(clothe)
  }

  return { wardrope, getWardrope, addClothe, removeClothe, editClothe, getFits, getClothesByCategory}
})


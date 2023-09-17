<script setup>
import { defineProps } from 'vue'
import ClotheCard from './ClotheCard.vue';

const props = defineProps({
    fit: {
        type: Object,
        required: true
    }
})
</script>

<template>
    <div class="box">
        <ClotheCard :clothe="fit.top"/>
        <ClotheCard :clothe="fit.bottom"/>
        <ClotheCard v-if="fit.outerwear != null" :clothe="fit.outerwear"/>
    </div>
</template>

<style scoped>
.box{
    width: 100vw;
    height: 100px;
    border: 1px solid black;
    padding: 10px;
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
}
</style>
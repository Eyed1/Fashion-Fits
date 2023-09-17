<script setup>
import { defineProps } from 'vue'
const props = defineProps({
    clothe: {
        type: Object,
        required: true
    }
})
</script>

<template>
    <form class="box">
        <img :src="clothe.imgLink">
        <input type="text" v-model="clothe.color">
        <input type="text" v-model="clothe.type">
        <button type="button" @click="$emit('close', clothe)">Close</button>
    </form>
</template>

<style scoped>
.box{
    position: fixed;
    left: 50vw;
    top: 20vh;
    transform: translate(-175px, 0);
    width: 350px;
    border: 1px solid black;
    padding: 10px;
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
}
</style>
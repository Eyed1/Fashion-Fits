<script setup>
import { defineProps } from 'vue'
const props = defineProps({
    imgLink: {
        type: String,
        required: true
    },
    text: {
        type: String,
        required: true
    },
    widthStr: {
        type: String,
        default: '250px'
    },
})
</script>

<template>
    <div class="box" :style="{ width: widthStr }">
        <img :src="imgLink">
        <p>{{ text }}</p>
    </div>
</template>

<style scoped>
.box{
    background-color: rgb(250, 250, 250);
    border: 0.2px solid black;
    box-shadow: 0px 0px 2px 0px rgba(0,0,0,0.75);
    border-radius: 10px;
    margin: 10px;
    padding: 10px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    cursor: pointer;
}

.box p{
    text-align: center;
}
</style>
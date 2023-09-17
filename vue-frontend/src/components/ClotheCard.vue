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
    <div class="box">
        <img :src="clothe.imgLink">
        <p>{{ `${clothe.color} ${clothe.type}` }}</p>
    </div>
</template>

<style scoped>
.box{
    width: 250px;
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
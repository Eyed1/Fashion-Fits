<script setup>
import { defineProps } from 'vue'
import { common_colors } from '../assets/palette.js'

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
        <p>{{ `${clothe.color} ${clothe.type}` }}</p>
        <div class="flex-row">
        <button id="delete" type="button" @click="$emit('deleteClose', clothe, true)">Delete</button>
        <button id="ok" type="button" @click="$emit('close', clothe, false)">OK</button>
        </div>
        
    </form>
</template>

<style scoped>
.box{
    position: fixed;
    left: 50vw;
    top: 20vh;
    transform: translate(-175px, 0);
    width: 350px;
    border: 0.2px solid black;
    box-shadow: 0px 0px 2px 0px rgba(0,0,0,0.75);
    border-radius: 10px;
    background-color: rgb(250, 250, 220);
    padding: 20px;
}

button{
    text-align: center;
    border: none;
    border-radius: 10px;
    padding: 10px;
    font-size: 25px;
    font-weight: bold;
    cursor: pointer;
}

button#delete{
    background-color: rgb(255, 150, 150);
    color: brown;
}

button#ok{
    background-color: rgb(150, 255, 150);
    color: green;
}

button#ok:hover{
    background-color: rgb(100, 255, 100);
}

button#delete:hover{
    background-color: rgb(255, 100, 100);
}

img{
    width: 100%;
    height: auto;
    margin: 10px 0px;
    margin-top: 15px;
}

.flex-row{
    display: flex;
    flex-direction: row;
    justify-content: space-evenly;
}

.box p{
    text-align: center;
    margin-top: 0;
    margin-bottom: 15px;
}

</style>
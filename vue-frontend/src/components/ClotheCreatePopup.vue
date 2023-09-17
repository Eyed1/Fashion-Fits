<script setup>
import { defineProps } from 'vue'
import { ref, computed } from 'vue';
import { common_colors } from '../assets/palette.js'
import ClotheCard from './ClotheCard.vue';
import {avatarMap, clothesMap} from '../assets/avatars.js'
import { useWardropeStore } from '../stores/wardropeStore';


const wardropeStore = useWardropeStore()

const clothe = ref({
    color: '#000000',
    type: '',
    category: '',
    imgLink: ''
})

const typeList = computed(() => {
    return clothesMap[clothe.value.category]
})

const makeClothe = () => {
    wardropeStore.addClothe(clothe.value)
    wardropeStore.getWardrope()
}

</script>

<template>
<form @submit="makeClothe">
    <h3>What type of clothing do you want to add?</h3>
    <div id="category">
        <ClotheCard class="item" @click="clothe.category='top'" :imgLink="avatarMap['top']" :color="clothe.color" text="Tops" :widthStr="'100px'" :class="{ selected:(clothe.category==='top') }"/>
        <ClotheCard class="item" @click="clothe.category='bottom'" :imgLink="avatarMap['bottom']" :color="clothe.color" text="Bottoms" :widthStr="'100px'" :class="{ selected:(clothe.category==='bottom') }"/>
        <ClotheCard class="item" @click="clothe.category='outerwear'" :imgLink="avatarMap['outerwear']" :color="clothe.color" text="Outerwear" :widthStr="'100px'" :class="{ selected:(clothe.category==='outerwear') }"/>
    </div>
    <div id="type">
        <ClotheCard class="item" v-for="type in typeList" :key="type" :imgLink="avatarMap[type]" :color="clothe.color" :text="type" :widthStr="'100px'" @click="clothe.type=type" :class="{ selected:(clothe.type===type) }"/>
    </div>
    <div id="colormeter">
        <p>Select a Color:</p>
        <vueticol v-model="clothe.color" :style="'circle'" :colors="common_colors"/>
    </div>
    <button id="submitButton" type="submit">Add</button>
</form>
</template>

<style scoped>
form{
    position: fixed;
    left: 50vw;
    top: 10vh;
    transform: translate(-250px, 0);
    background-color: rgb(250, 235, 250);
    border-radius: 20px;
    border: 0.6px solid black;
    padding: 25px;
    box-shadow: 0px 0px 8px 0px rgba(0,0,0,0.75);
    width: 500px;
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    align-items: center;
}
#category{
    margin-top: 25px;
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: space-evenly;
}

#colormeter{
    margin-top: 25px;
    display: flex;
    flex-direction: row;
}

#colormeter p{
    margin-right: 25px;
}




#type{
    margin-top: 25px;
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: space-evenly;
    overflow-x: scroll;
}

#category .item{
    width: 30%;
    border: 0.2px solid black;
    background-color: rgb(250, 250, 220);
}

#type .item{
    width: 30%;
    border: 0.2px solid black;
    background-color: rgb(250, 250, 220);
}

#type .item:hover{
    background-color: rgb(250, 250, 150);
}

#category .item:hover{
    background-color: rgb(250, 250, 150);
}

#category .selected{
    background-color: rgb(250, 250, 150);
}
#type .selected{
    background-color: rgb(250, 250, 150);
}


button#submitButton{
    margin-top: 25px;
    text-align: center;
    border: none;
    border-radius: 10px;
    padding: 10px;
    font-size: 25px;
    font-weight: bold;
    cursor: pointer;
    background-color: rgb(150, 255, 150);
    color: green;
}

button#submitButton:hover{
    background-color: rgb(100, 255, 100);
}

</style>

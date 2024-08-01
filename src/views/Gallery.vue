<script setup lang="ts">

import { ref } from 'vue'

import Galleria from 'primevue/galleria';


let image_obj = []

for (let i = 1; i < 13 ; i++) {
    image_obj.push({
        itemImageSrc: "src/assets/images/gallery/" + i.toString() + ".jpg",
        thumbnailImageSrc: "src/assets/images/gallery_thmb/" + i.toString() + ".jpg",
        alt: "image: " + i.toString()})
} 

const images = ref(image_obj)

const activeIndex = ref(0)

const responsiveOptions = null
const displayCustom = ref(true)
const position = ref("button")

</script>

<template>
  <div class="gallery">
    <Galleria :value="images" :responsiveOptions="responsiveOptions" :numVisible="5" :thumbnailsPosition="position" containerStyle="max-width: 640px">
        <template #item="slotProps">
            <img :src="slotProps.item.itemImageSrc" :alt="slotProps.item.alt" style="width: 100%; display: block" />
        </template>
        <template #thumbnail="slotProps">
            <div class="grid gap-4 justify-center">
                <img :src="slotProps.item.thumbnailImageSrc" :alt="slotProps.item.alt" style="width: 100%; display: block;" />
            </div>
        </template>
    </Galleria>
</div>

</template>

<style>
</style>


<template>
    <div>
        <SimpleFormGetData mainText="Quantity Boxes" route="/getqty" placeholder="Reference Article"/>
    </div>
</template>

<script>
import SimpleFormGetData from '../../components/SimpleFormGetData.vue';
    export default {
        components:{
            SimpleFormGetData:SimpleFormGetData
        }
    }
</script>

<style scoped>

</style>
<template>
    <div>
        <SimpleFormGetData mainText="Article quantity in stock" route="/getqty" placeholder="Reference Article"/>
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
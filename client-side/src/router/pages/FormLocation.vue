<template>
    <div>
         <SimpleFormWithTable mainText="Location Boxes" route="/getlocation" placeholder="Reference Article" />
    </div>
</template>

<script>
import SimpleFormWithTable from '../../components/SimpleFormWithTable.vue';
    export default {
        components:{
         SimpleFormWithTable:SimpleFormWithTable
        }
    }
</script>

<style scoped>

</style>
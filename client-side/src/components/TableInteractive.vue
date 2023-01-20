<template>
    <div>
        <vue-good-table ref="test" :columns="columns" :rows="rowData" />
    </div>
</template>

<script>
import { VueGoodTable } from 'vue-good-table-next';
export default {
    components: { VueGoodTable },
    props: {
        columns: {
            type:Array,
            required: true,
        },
        rowData: {
            type:Array,
            required: true,
        },
    },

}
</script>

<style scoped>

</style>
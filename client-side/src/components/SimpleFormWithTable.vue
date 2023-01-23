<template>
    <div>
        <h1>{{mainText}}</h1>
        <p>
            <input v-model='reference' :placeholder="placeholder" />
        </p>
        <p>
            <Button @click="getData" :disable="disable" />
        </p>
        <div v-if="showTable">
            <TableInteractive class='table' :columns="columns" :rowData="rowData" />
        </div>
    </div>
</template>

<script>
import Button from './Button.vue';
import axios from 'axios';
import TableInteractive from './TableInteractive.vue';
import getPostPath from '../utils/helper'

export default {
    props:{
        mainText :String,
        placeholder:{
            type:String,
            default:"Ref"
        },
        route:{
            type:String,
            required:true
        }
    },
    data() {
        return {
            rowData:[],
            columns:[],
            showTable: false,
            disable:false,
            reference:''
        }
    },
    mounted() {
        // to construct the columns frame only once
        fetch(getPostPath(this.route))
            .then(res => res.json())
            .then(response => {
                let cols = response.schema.fields
                cols.map(col => {
                    if (col.name !== 'index') {
                        this.generateColumnFromObjectKeys(col.name)}
                    })
                
            })
    },
    methods: {
        generateColumnFromObjectKeys (key){            
            this.columns.push({
                label: key,
                field: key,
                filterable: true,
                filterOptions: {
                        enabled: true,
                    }
            })
        },
        getData(){
            axios.post(getPostPath(this.route), this.reference.toUpperCase(), {
                headers: { 'Content-Type': 'application/json' },
            })
                .then(response => {
                    this.showTable=true;
                    this.rowData = response.data.data;
                    
                })
                .catch(error => {
                    console.log(error)
                })
        }
    },
    components: {
        Button: Button,
        TableInteractive:TableInteractive
    }

}
</script>

<style scoped>

.table{
    padding: 0%;
}
</style>
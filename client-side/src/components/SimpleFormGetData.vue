<template>
    <div>
       <h1> {{mainText}} </h1> 
        <p>
            <input v-model='reference' :placeholder="placeholder" />
        </p>
        <p>
            <Button @click="getData" :disable="disable" />
        </p>
        <h3> {{ answerServer }}</h3>

    </div>
</template>

<script>
import Button from './Button.vue';
import axios from 'axios';
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
            disable:false,
            reference:'',
            answerServer:''
        }
    },

    methods: {
        getData(){
            axios.post(getPostPath(this.route), this.reference.toUpperCase(), {
                headers: { 'Content-Type': 'application/json',
                            "Access-Control-Allow-Origin": "*" },
            })
                .then(response => {
                    this.answerServer = response.data
                    
                })
                .catch(error => {
                    console.log(error)
                })
        }
    },
    components: {
        Button: Button,
    }

}
</script>

<style scoped>

</style>
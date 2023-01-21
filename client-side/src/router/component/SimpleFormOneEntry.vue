<template>
    <div>
        <p>
            <input v-model='reference' placeholder="Ref. Article here" />
        </p>

        <Button @click="getData" :disable="disable"/>
    </div>
</template>

<script>
import Button from './Button.vue';
import axios from 'axios';
export default {

    data() {
        return {
            disable:false,
            reference:''
        }
    },
    methods: {
        getData(){
            axios.post("http://localhost:5000/getlocation", this.reference, {
                headers: { 'Content-Type': 'application/json' },
            })
                .then(response => {
                    console.log(response)
                    
                })
                .catch(error => {
                    console.log(error)
                })
        }
    },
    components:{
        Button:Button
    }

}
</script>

<style scoped>

</style>
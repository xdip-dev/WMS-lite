<template>
    <div>
        <p ref="linkStatus">
           <h1> {{statusMsg}}</h1>
        </p>
        <p>
            <input v-model='barCodeBoxe' type="text" placeholder="Scan boxe" />
        </p>
        <p>
            <input v-model='barcodeLocation' type="text" placeholder="Scan location" />
        </p>
        <Button :disabled="disable" @click="submitData" text="Link !" />
    </div>
</template>

<script>
import axios from 'axios';
import Button from '../../components/Button.vue';
import { ref } from 'vue';
export default {
    data() {
        return {
            payload: {
                'barCodeBoxe': this.barCodeBoxe,
                'barcodeLocation': this.barcodeLocation,
            },
            barCodeBoxe: '',
            barcodeLocation: '',
            statusMsg:'Link your barcodes',
            disable:false

        }
    },

    methods: {
        submitData() {
            this.payload.barCodeBoxe = this.barCodeBoxe
            this.payload.barcodeLocation = this.barcodeLocation
            this.disable=true

            // Send data to the server in a JSON format
            axios.post("http://localhost:5000/linkboxloc", this.payload, {
                headers: { 'Content-Type': 'application/json' },
            })
                .then(response => {
                    console.log(response)
                    this.statusMsg=response.data
                    this.disable=false
                    
                })
                .catch(error => {
                    console.log(error)
                    this.statusMsg='Something went wrong, try to reload the page :('
                })
                    .then(
                        this.barCodeBoxe='',
                        this.barcodeLocation=''
                    )


        }
    },
    components:{
        Button:Button
    }

}
</script>

<style scoped>

</style>
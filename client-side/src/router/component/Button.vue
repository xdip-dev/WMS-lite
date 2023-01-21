<template>
    <div>
        <button :disabled="disable">
            {{ text }}
        </button>
    </div>
</template>

<script>
    export default {
        props:{
            text:{
                type:String,
                default:'Go !'
            },
            disable:{
                type:Boolean,
                default:false
            }
        },
        data() {
        return {


        }
    },

    methods: {

    }
    }
</script>

<style scoped>

</style>
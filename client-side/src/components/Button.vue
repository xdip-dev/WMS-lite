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
button {
  border-radius: 8px;
  border: 1px solid transparent;
  padding: 0.6em 1.2em;
  font-size: 1em;
  font-weight: 500;
  font-family: inherit;
  cursor: pointer;
  transition: border-color 0.25s;
  margin: 3px;
  background-color: #55d49b;
}
button:hover {
  border-color: #646cff;
}
button:focus,
button:focus-visible {
  outline: 4px auto -webkit-focus-ring-color;
}
</style>
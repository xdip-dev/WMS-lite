<template>
  <div>
    <Navbar />
    <div class="routerview">
      <RouterView />
    </div>
  </div>
</template>

<script>
import { RouterView } from "vue-router";
import Navbar from "./components/Navbar.vue"
export default {
  components: {
    Navbar: Navbar
  }

}
</script>

<style  scoped>
.routerview {
  margin: 0 auto;
  padding: 2rem;
  text-align: center;
}
</style>
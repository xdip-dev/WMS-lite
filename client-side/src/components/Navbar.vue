<template>
    <div>
        <nav class="navbar navbar-expand-lg ">
            <div class="container-fluid">
                <span class="navbar-brand mb-0 h1">Filtroptic <i class="fa-solid fa-glasses"></i></span>
            </div>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <RouterLink class="nav-link active" to="/">Home</RouterLink>
                    </li>
                </ul>
            </div>
        </nav>
    </div>
</template>

<script>
import { RouterLink } from "vue-router";

</script>

<style scoped>
.navbar {
background-color: #55d49b;
padding:0px 20px;
}
</style>
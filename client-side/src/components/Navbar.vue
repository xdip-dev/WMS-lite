<template>
    <div>
        <nav class="navbar navbar-expand-lg ">
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <RouterLink class="nav-link active" to="/">Link code</RouterLink>
                    </li>
                    <li class="nav-item">
                        <RouterLink class="nav-link active" to="/location">Location</RouterLink>
                    </li>
                    <li class="nav-item">
                        <RouterLink class="nav-link active" to="/quantity">Quantity</RouterLink>
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
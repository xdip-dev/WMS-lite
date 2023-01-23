<template>
    <div>
        <!-- <nav class="navbar navbar-expand-lg ">
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <RouterLink class="nav-link active" to="/">Link code</RouterLink>
                    </li>
                    <li class="nav-item">
                        <RouterLink class="nav-link active" to="/location">Location</RouterLink>
                    </li>
                    <li class="nav-item">
                        <RouterLink class="nav-link active" to="/quantity">Quantity</RouterLink>
                    </li>
                    <li class="nav-item">
                        <RouterLink class="nav-link active" to="/rmvstock">Remove</RouterLink>
                    </li>

                </ul>
            </div>
        </nav> -->
        <nav class="navbar navbar-expand-lg bg-light ">
            <div class="container-fluid">
                <a class="navbar-brand" href="#">Navigation</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                    data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false"
                    aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
                    <div class="navbar-nav">
                        <RouterLink class="nav-link " to="/">Link code</RouterLink>
                        <RouterLink class="nav-link " to="/location">Location</RouterLink>
                        <RouterLink class="nav-link " to="/quantity">Quantity</RouterLink>
                        <RouterLink class="nav-link " to="/rmvstock">Remove</RouterLink>
                    </div>
                </div>
            </div>
        </nav>
    </div>
</template>

<script>
import { RouterLink } from "vue-router";

</script>

<style scoped>
a.router-link-active{
    background-color: #55d49b;
}
.navbar {
    padding: 0px 20px;
}
</style>
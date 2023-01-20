import {createRouter, createWebHistory} from "vue-router";
import Reception from "./pages/Reception.vue";

const router =  createRouter(
    {
    history: createWebHistory(),
    routes:[
        {
            path:'/',
            component : Reception,
        },
    ]
    }
)

export default router;
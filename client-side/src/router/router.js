import {createRouter, createWebHistory} from "vue-router";
import FormInsert from "./pages/FormInsert.vue";
import FormLocation from "./pages/FormLocation.vue";
import FormQuantity from "./pages/FormQuantity.vue";

const router =  createRouter(
    {
    history: createWebHistory(),
    routes:[
        {
            path:'/',
            component : FormInsert,
        },
        {
            path:'/location',
            component : FormLocation,
        },
        {
            path:'/quantity',
            component : FormQuantity,
        },
    ]
    }
)

export default router;
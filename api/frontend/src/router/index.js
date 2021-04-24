import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Home',
        meta:{guest:true},
        component: Home
    },
    {
        path: '/about',
        name: 'About',
        meta:{guest:true},
        component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
    },
    {
        path: '/classify',
        name: 'Classify',
        meta:{guest:false},
        component: () => import('../views/Classify.vue')
    }
]

const router = new VueRouter({
    routes
})

router.beforeEach((to, from, next) => {
    if (!to.meta.guest) {
        if (localStorage.getItem('token') == null) {
            return next({path:'/'});
        }
    }
    return next();
});

export default router
import Vue from 'vue';
import Router from 'vue-router';

Vue.use(Router);

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            redirect: '/texts'
        },
        {
            path: '/texts',
            name: 'texts',
            component: () => import('../views/TextList.vue'),
            meta: { title: 'Texts', display: true }
        },
        {
            path: '/text',
            name: 'text',
            component: () => import('../views/Text.vue'),
            meta: { title: 'Text', display: true },
            props: true
        },
        {
            path: '/similarities',
            name: 'similarities',
            component: () => import('../views/Similarity.vue'),
            meta: { title: 'Similarities', display: true },
            props: true
        }
    ]
});

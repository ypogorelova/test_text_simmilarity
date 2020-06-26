import Vue from 'vue';
import App from './App.vue';
import router from './plugins/router';
import vuetify from './plugins/vuetify';
import './plugins/components';
import '@babel/polyfill';

Vue.config.productionTip = false;

new Vue({
    router,
    vuetify,
    render: h => h(App)
}).$mount('#app');

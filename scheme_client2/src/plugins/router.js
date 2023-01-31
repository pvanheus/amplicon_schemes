import Vue from "vue";
import Router from "vue-router";
import SchemeSubmit from "@/components/SchemeSubmit";
import SchemeList from "@/components/SchemeList";
import SchemeDetail from "@/components/SchemeDetail";
import SchemeDetailBootstrap from "@/components/SchemeDetailBootstrap.vue";
Vue.use(Router);

export default new Router({
    routes: [
        { path: '/', component: SchemeSubmit },
        { path: '/list', component: SchemeList },
        { path: '/detail', component: SchemeDetail, props: {
            url: 'https://raw.githubusercontent.com/pha4ge/primer-schemes/main/sars-cov-2/artic/v4.1/info.yaml'
        }},
        { path: '/detail_b', component: SchemeDetailBootstrap, props: {
                url: 'https://raw.githubusercontent.com/pha4ge/primer-schemes/main/sars-cov-2/artic/v4.1/info.yaml'
        }}
    ],
    mode: "history"
});

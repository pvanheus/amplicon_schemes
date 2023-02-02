import Vue from "vue";
import Router from "vue-router";
import SchemeSubmit from "@/components/SchemeSubmit";
import SchemeList from "@/components/SchemeList";
Vue.use(Router);

export default new Router({
    routes: [
        { path: '/add', component: SchemeSubmit },
        { path: '/list', component: SchemeList },
    ],
    mode: "history"
});

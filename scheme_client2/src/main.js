import Vue from 'vue'
import router from "@/plugins/router";
import vuetify from "@/plugins/vuetify";

Vue.config.productionTip = false

import App from './App';

new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount("#app");


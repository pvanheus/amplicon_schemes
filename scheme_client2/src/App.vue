<template>
  <v-app>
    <v-app-bar color="blue" class="flex-grow-0" app>
      <v-app-bar-nav-icon @click="drawer = true"> </v-app-bar-nav-icon>
      <v-toolbar-title class="title">Primer Schemes</v-toolbar-title>
    </v-app-bar>
      <v-navigation-drawer v-model="drawer" app temporary>
        <v-list  dense nav>
          <router-link v-for="item in nav_items" :key="item.title" :to="item.link">
            <v-list-item>
              <v-list-item-icon>
                <v-icon>{{ item.icon }}</v-icon>
              </v-list-item-icon>
              <v-list-item-content>
                <v-list-item-title>{{ item.title }}</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </router-link>
        </v-list>
      </v-navigation-drawer>
    <v-main>
      <v-container fluid>
        <v-row class="fill-height">
          <v-col>
            <transition name="fade">
              <router-view></router-view>
            </transition>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
    <v-footer>
      Footer goes here
    </v-footer>
  </v-app>
</template>

<script>

export default {
  name: 'App',
  data: () => ({
    drawer: false,
    nav_items: [
      { title: 'Scheme List', icon: 'mdi-eye', link: '/' },
      { title: 'Add a Scheme', icon: 'mdi-plus', link: '/add' },
    ]
  })
};
</script>

<style>
</style>

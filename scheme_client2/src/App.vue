<template>
  <v-app>
    <v-app-bar color="blue" class="flex-grow-0" app dark>
      <v-app-bar-title class="title">Primer Schemes</v-app-bar-title>
    </v-app-bar>
    <v-main>
      <router-view></router-view>
    </v-main>
    <v-navigation-drawer app>
      <v-list  dense nav>
        <router-link v-for="item in nav_items" :key="item.title" :to="item.link">
          <v-list-item link>
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
  </v-app>
</template>

<script>

export default {
  name: 'App',
  data: () => ({
    nav_items: [
      { title: 'Home', icon: 'mdi-home', link: '/' },
      { title: 'Scheme List', icon: 'mdi-eye', link: '/list' },
      { title: 'Scheme Detail', link: '/detail' }
    ]
  })
};
</script>

<style>
.v-app-bar-title__content{
  width: 200px;
}
</style>

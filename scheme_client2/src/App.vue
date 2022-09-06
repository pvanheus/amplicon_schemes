<template>
  <v-app>
    <v-navigation-drawer permanent>
      <v-list>
        <v-list-item>
          <v-list-item-content>
            <router-link to="/">Home</router-link>
          </v-list-item-content>
        </v-list-item>
        <v-list-item>
          <v-list-item-content>
            <v-list-item-title><router-link to="/list">List</router-link></v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <router-view></router-view>
  </v-app>
</template>

<script>

export default {
  name: 'App',
};
</script>

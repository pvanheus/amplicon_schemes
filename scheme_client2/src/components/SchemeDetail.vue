<template>
  <v-card class="fill-height card">
    <v-card-title>Scheme Name:&nbsp; {{detail.name}}</v-card-title>
    <v-card-text>
      <strong label>Organism:</strong> {{this.detail.organism}}
      <div v-if="detail.organism_aliases">
          <strong>Organism Aliases:</strong>
          <v-list dense v-for="alias in detail.organism_aliases" :key="alias" class="pa-0 ma-0">
            <v-list-item>
              <v-list-item-content>
                  {{alias}}
              </v-list-item-content>
            </v-list-item>
          </v-list>
      </div>
      <strong>Amplicon Size: </strong> &nbsp;{{detail.amplicon_size}}
      <div v-if="detail.aliases">
        <strong>Scheme Name Aliases:</strong>
        <v-list v-for="alias in detail.aliases" v-bind:key="alias">
          <v-list-item>{{alias}}</v-list-item>
        </v-list>
      </div>
      <div>
        <strong>Scheme Developers:</strong>
        <v-list v-for="developer in detail.developers" v-bind:key="developer.name">
          <v-list-item>
            <v-list-item-content>
              <v-list-item-title>
                <span>{{developer.name}}</span> <a v-if="developer.url" target="_blank" :href="developer.url"><v-icon>mdi-link</v-icon></a>
              </v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </div>
      <div v-if="detail.vendors">
        <strong>Primer Vendors:</strong>
        <v-list dense v-for="vendor in detail.vendors" v-bind:key="vendor.name">
          <v-list-item v-if="vendor.url">
            <v-list-item-content>
              <v-list-item-title>
                <span>{{vendor.name}}</span> <a v-if="vendor.url" target="_blank" :href="vendor.url"><v-icon>mdi-link</v-icon></a>
              </v-list-item-title>
            </v-list-item-content>
          </v-list-item>
          <v-list-item v-else>{{vendor.name}}<span v-if="vendor.kit_name">: {{vendor.kit_name}}</span></v-list-item>
        </v-list>
      </div>
      <div v-if="detail.citations">
        <strong>Citations:</strong>
        <v-list v-for="citation in detail.citations" v-bind:key="citation">
          <v-list-item><a :href="citation">{{citation}}</a></v-list-item>
        </v-list>
      </div>
      <div v-if="detail.derived_from">
        <strong>Derived from:</strong> &nbsp;<span v-html="detail.derived_from"></span>
      </div>
      <strong>Link to repository</strong> <a :href="detail.repository_url" target="_blank"><v-icon>mdi-link</v-icon></a>
      <v-card-actions>
        <v-btn @click="downloadScheme">Download</v-btn>
      </v-card-actions>
    </v-card-text>
  </v-card>
</template>

<script>
const yaml = require('js-yaml');

export default {
  name: "SchemeDetail.vue",
  props: {
    url: String,
  },
  data() {
    return {
      detail: null
    }
  },
  methods: {
    downloadScheme: () => {

    }
  },
  mounted() {
    fetch(this.url).then(async response => {
      this.detail = yaml.load(await response.text(), {schema: this.JSON_SCHEMA});
    }).catch();
  }
}
</script>

<style scoped>

</style>

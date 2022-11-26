<template>
  <v-card>
    <v-card-title>Scheme Name:&nbsp; <a :href="detail.repository_url">{{detail.name}}</a></v-card-title>
    <v-card-text>
      <v-row>
        <strong>Organism:</strong> {{this.detail.organism}}
      </v-row>
      <v-row v-if="detail.organism_aliases">
          <strong>Organism Aliases:</strong>
          <v-list v-for="alias in detail.organism_aliases" v-bind:key="alias">
            <v-list-item>{{alias}}</v-list-item>
          </v-list>
      </v-row>
      <v-row>
        <strong>Amplicon Size: </strong> &nbsp;{{detail.amplicon_size}}
      </v-row>
      <v-row v-if="detail.aliases">
        <strong>Scheme Name Aliases:</strong>
        <v-list v-for="alias in detail.aliases" v-bind:key="alias">
          <v-list-item>{{alias}}</v-list-item>
        </v-list>
      </v-row>
      <v-row>
        <strong>Scheme Developers:</strong>
        <v-list v-for="developer in detail.developers" v-bind:key="developer.name">
          <v-list-item v-if="developer.url"><a :href="developer.url">{{developer.name}}</a></v-list-item>
          <v-list-item v-else>{{developer.name}}</v-list-item>
        </v-list>
      </v-row>
      <v-row v-if="detail.vendors">
        <strong>Primer Vendors:</strong>
        <v-list v-for="vendor in detail.vendors" v-bind:key="vendor.name">
          <v-list-item v-if="vendor.url"><a :href="vendor.url">{{vendor.name}}<span v-if="vendor.kit_name">: {{vendor.kit_name}}</span></a></v-list-item>
          <v-list-item v-else>{{vendor.name}}<span v-if="vendor.kit_name">: {{vendor.kit_name}}</span></v-list-item>
        </v-list>
      </v-row>
      <v-row v-if="detail.citations">
        <strong>Citations:</strong>
        <v-list v-for="citation in detail.citations" v-bind:key="citation">
          <v-list-item><a :href="citation">{{citation}}</a></v-list-item>
        </v-list>
      </v-row>
      <v-row v-if="detail.derived_from">
        <strong>Derived from:</strong> &nbsp;{{detail.derived_from}}
      </v-row>
      <v-row>
        <v-card-actions>
          <v-btn @click="downloadScheme">Download</v-btn>
        </v-card-actions>
      </v-row>
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

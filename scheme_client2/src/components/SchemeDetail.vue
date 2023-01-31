<template>
  <v-container fluid>
    <v-row :class="spacer_class">
      <h3>Scheme Name:&nbsp; {{detail.name}}</h3>
    </v-row>
    <v-col class="sm6">
      <v-row :class="spacer_class">
        <strong label>Organism:</strong> {{this.detail.organism}}
      </v-row>
      <row :class="spacer_class" v-if="detail.organism_aliases">
        <strong>Organism Aliases:</strong>
        <v-list dense v-for="alias in detail.organism_aliases" :key="alias" class="pa-0 ma-0">
          <v-list-item>
            <v-list-item-content>
              {{alias}}
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </row>
      <v-row :class="spacer_class">
        <strong>Amplicon Size: </strong> &nbsp;{{detail.amplicon_size}}
      </v-row>
      <v-row :class="spacer_class" v-if="detail.aliases">
        <strong>Scheme Name Aliases:</strong>
        <v-list dense v-for="alias in detail.aliases" v-bind:key="alias" class="pa-0 ma-0">
          <v-list-item>{{alias}}</v-list-item>
        </v-list>
      </v-row>
    </v-col>
    <v-col class="sm6">
      <v-row :class="spacer_class">
        <strong>Scheme Developers:</strong>
        <v-list dense v-for="developer in detail.developers" v-bind:key="developer.name">
          <v-list-item>
            <v-list-item-content>
              <v-list-item-title>
                <span>{{developer.name}}</span> <a v-if="developer.url" target="_blank" :href="developer.url"><v-icon>mdi-link</v-icon></a>
              </v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-row>
      <v-row :class="spacer_class" v-if="detail.vendors">
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
      </v-row>
      <v-row :class="spacer_class" v-if="detail.citations">
        <strong>Citations:</strong>
        <v-list dense v-for="citation in detail.citations" v-bind:key="citation">
          <v-list-item><a :href="citation">{{citation}}</a></v-list-item>
        </v-list>
      </v-row>
      <v-row :class="spacer_class" v-if="detail.derived_from">
        <strong>Derived from:</strong> &nbsp;<span v-html="detail.derived_from"></span>
      </v-row>
      <v-row :class="spacer_class">
        <strong>Link to repository</strong> <a :href="detail.repository_url" target="_blank"><v-icon>mdi-link</v-icon></a>
      </v-row>
      <v-row :class="spacer_class">
        <v-btn @click="downloadScheme">Download</v-btn>
      </v-row>
    </v-col>
  </v-container>
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
      spacer_class: "ma-1",
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

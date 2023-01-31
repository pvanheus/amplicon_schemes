<template>
  <v-container v-if="detail" fluid>
    <v-row :class="rowClass">
      <v-col class="sm1">
        <h2>
          Scheme Name
          <span class="font-weight-light">{{ detail.name }}</span>
        </h2>
      </v-col>
      <v-col class="sm1" v-if="detail.aliases">
        <h3>Scheme Aliases</h3>
        <v-list v-for="alias in detail.aliases" :key="alias">
          <v-list-item>{{ alias}}</v-list-item>
        </v-list>
      </v-col>
    </v-row>
    <v-row :class="rowClass">
      <v-col>
        <h2>
          Organism
          <span class="font-weight-light"> {{ detail.organism }}</span>
        </h2>
      </v-col>
      <v-col>
        <h3>Organism Aliases</h3>
        <v-list>
          <v-list-item>nCov-2019</v-list-item>
        </v-list>
      </v-col>
    </v-row>
    <v-row :class="rowClass">
      <v-col>
        <h2>
          Amplicon Size
          <span class="font-weight-light">{{ detail.amplicon_size}}</span>
        </h2>
      </v-col>
    </v-row>
    <v-row :class="rowClass">
      <v-col>
        <h3>
          <div v-if="detail.developers && detail.developers.length === 1">Scheme Developer
            <span  class="font-weight-light"><a :href="detail.developers[0].url">{{ detail.developers[0].name}}</a></span>
          </div>
          <div v-else>
            Scheme Developers
            <v-list>
              <v-list-item v-for="developer in detail.developers" :key="developer.name">
                <span  class="font-weight-light"><a :href="developer.url">{{ developer.name}}</a></span>
              </v-list-item>
            </v-list>
          </div>
        </h3>
      </v-col>
    </v-row>
    <v-row :class="rowClass">
      <v-col>
        <h3>
          <div v-if="detail.vendors && detail.vendors.length === 1">Primer Vendor
            <span  class="font-weight-light"><a :href="detail.vendors[0].url">{{ detail.vendors[0].name}}</a></span>
          </div>
          <div v-else>
            Primer Vendors
            <v-list>
              <v-list-item v-for="vendor in detail.vendors" :key="vendor.name">
                <span  class="font-weight-light"><a :href="vendor.url">{{ vendor.name}}</a></span>
              </v-list-item>
            </v-list>
          </div>
        </h3>
      </v-col>
    </v-row>
    <v-row :class="rowClass">
      <v-col>
        <h3>
          <div v-if="detail.citations && detail.citations.length === 1">Citation
            <span  class="font-weight-light"><a :href="detail.citations[0]">{{ detail.citations[0] }}</a></span>
          </div>
          <div v-else>
            Citations
            <v-list>
              <v-list-item v-for="citation in detail.citations" :key="citation">
                <span class="font-weight-light"><a :href="citatioin">{{ citation }}</a></span>
              </v-list-item>
            </v-list>
          </div>
        </h3>
      </v-col>
    </v-row>
    <v-row :class="rowClass">
      <v-col>
        <h3 v-if="detail.derived_from">Derived from
          <span class="font-weight-light">{{ detail.derived_from }}</span>
        </h3>
      </v-col>
    </v-row>
    <v-row :class="rowClass">
      <v-col>
        <v-btn>Download</v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
const yaml = require('js-yaml');

export default {
  name: "SchemeDetailBootstrap.vue",
  props: {
    url: String,
  },
  data() {
    return {
      spacer_class: "ma-1",
      detail: null,
      rowClass: "mt-0 mb-0"
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

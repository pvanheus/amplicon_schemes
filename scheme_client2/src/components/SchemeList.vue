<template>
  <v-container>
    <v-text-field
        v-model="search"
        label="Search"
    ></v-text-field>
    <v-data-table
        :items="schemes"
        item-key="name"
        :headers="headers"
        :search="search"
      >
      <template #item.bed_url="{ item }">
        <a target="_blank" :href="item.bed_url">
          BED file
        </a>
      </template>
    </v-data-table>
  </v-container>
</template>

<script>
const yaml = require('js-yaml');

export default {
  name: "SchemeList",
  data() {
    return {
      search: '',
      schemes: Array(),
      headers: [
        {
          text: 'Name',
          value: 'name'
        },
        {
          text: 'Organism',
          value: 'organism'
        },
        {
          text: 'Amplicon Size',
          value: 'amplicon_size'
        },
        {
          text: 'BED',
          value: 'bed_url',
          filterable: false
        }
      ]
    }
  },
  mounted() {
    const url = "https://raw.githubusercontent.com/pvanheus/amplicon_schemes/main/schemes.yml";
    fetch(url).then(async response => {
          const result =  yaml.load(await response.text());
          this.schemes = result;
        }
    )
  }
}
</script>

<style scoped>

</style>

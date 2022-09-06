<template>
  <div>
    <v-data-table
        :items="schemes"
        :headers="headers">
      <template #item.bed_url="{ item }">
        <a target="_blank" :href="item.bed_url">
          BED file
        </a>
      </template>
    </v-data-table>
  </div>
</template>

<script>
const yaml = require('js-yaml');

export default {
  name: "SchemeList",
  data() {
    return {
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
          value: 'bed_url'
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

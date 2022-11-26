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
      <template #item.versions="{ item }">
        <span v-for="version in item.versions" :key="version.version">
          <strong v-if="version.version === item.latest_version">
            {{version.version}}
          </strong>
          <span v-else> {{version.version}} </span>
          <span>
            <v-dialog
                v-if="isKnown(item.name, version.version)"
                v-model="dialog"
                width="500"
              >
              <template v-slot:activator="{ on, attrs }">
                <v-icon small
                        v-bind="attrs"
                        v-on="on"
                >mdi-information-outline</v-icon>
              </template>

              <v-card >
                <v-card-title>
                  Title
                </v-card-title>

                <v-card-text>
                  Details
                </v-card-text>

                <v-card-actions>
                  <v-btn
                    color="primary"
                    text
                    @click="dialog = false"
                    >
                    Close
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </span>
        </span>

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
      dialog: false,
      search: '',
      schemes: Array(),
      scheme_details: Object(),
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
          text: 'Latest Version',
          value: 'latest_version'
        },
        { text: 'Versions',
          value: 'versions'
        }
      ]
    }
  },
  mounted() {
    const url = "https://raw.githubusercontent.com/PHA4GE/primer-schemes/main/index.yml";
    fetch(url).then(async response => {
          const result = yaml.load(await response.text());
          this.schemes = result.schemes;
          this.loadSchemeDetails(this.schemes);
        }
    ).catch();
  },
  methods: {
    isKnown: function(name, version) {
      const lookupName = name.toString().toLowerCase();
      const lookupVersion = version.toString().toLowerCase();
      return this.scheme_details[lookupName] && this.scheme_details[lookupName][lookupVersion]
    },
    loadSchemeDetails: function (schemes) {
      schemes.forEach(scheme => {
        this.$set(this.scheme_details, scheme.name.toLowerCase(), {});
        scheme.versions.forEach(v => {
          const url = v.repository.replace('github.com', 'raw.githubusercontent.com') + '/scheme.yaml';
          fetch(url).then(async response => {
            if (response.status === 200) {
              const result = yaml.load(await response.text());
              this.$set(this.scheme_details[scheme.name.toLowerCase()], v.version.toLowerCase(), result);
            }
          })
        });
      })
    }
  }
}
</script>

<style scoped>

</style>

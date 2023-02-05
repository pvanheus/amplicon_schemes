<template>
  <v-container>
    <v-data-table
        :items="schemes"
        item-key="name"
        :headers="headers"
        :search="search"
        :expanded.sync="expanded"
        single-expand
        show-expand
    >
      <template v-slot:top>
        <v-toolbar flat>
          <v-spacer></v-spacer>
        <v-text-field
            v-model="search"
            label="Search"
        ></v-text-field>
        </v-toolbar>
      </template>
      <template v-slot:item.latest_version="{ item }">
        {{item.latest_version}}
        <span v-if="isKnown(item.name, item.latest_version)">
            <v-dialog

                v-model="dialog[dialogKey(item.name, item.latest_version)]"
                width="800"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-icon small
                        v-bind="attrs"
                        v-on="on"
                >mdi-information-outline</v-icon>
              </template>

              <div>
                <v-card>
              <scheme-detail :detail="getDetail(item.name, item.latest_version)" />
                  <v-btn
                      color="primary"
                      text
                      @click="dialog[dialogKey(item.name, item.latest_version)] = false"
                  >
                    Close
                  </v-btn>
                  </v-card>
              </div>
            </v-dialog>
          </span>
      </template>
      <template v-slot:expanded-item="{ headers, item }">
        <td :colspan="headers.length">
          All versions:
        <span v-for="version in item.versions" :key="version.version">
          <strong v-if="item.latest_version && version.version === item.latest_version">
            {{version.version}}
          </strong>
          <span v-else> {{version.version}} </span>
          <span>
            <v-dialog
                v-if="isKnown(item.name, version.version)"
                v-model="dialog[dialogKey(item.name, version.version)]"
                width="800"
              >
              <template v-slot:activator="{ on, attrs }">
                <v-icon small
                        v-bind="attrs"
                        v-on="on"
                >mdi-information-outline</v-icon>
              </template>

              <div>
                <v-card>
              <scheme-detail :detail="getDetail(item.name, version.version)" />
                  <v-btn
                    color="primary"
                    text
                    @click="dialog[dialogKey(item.name, version.version)] = false"
                    >
                    Close
                  </v-btn>
                  </v-card>
              </div>
            </v-dialog>
          </span>
        </span>
        </td>
      </template>
    </v-data-table>
  </v-container>
</template>

<script>
import SchemeDetail from "@/components/SchemeDetail.vue";

const yaml = require('js-yaml');

export default {
  name: "SchemeList",
  components: {SchemeDetail},
  data() {
    return {
      dialog: Object(),
      search: '',
      schemes: Array(),
      scheme_details: Object(),
      expanded: [],
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
          value: 'latest_version',
          sortable: false
        },
        { text: '', value: 'data-table-expand' },
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
      if (name === undefined || version === undefined) {
        return false
      }
      const lookupName = name.toString().toLowerCase();
      const lookupVersion = version.toString().toLowerCase();
      return this.scheme_details[lookupName] && this.scheme_details[lookupName][lookupVersion]
    },
    dialogKey: function(name, version) {
      const lookupName = name.toString().toLowerCase();
      const lookupVersion = version.toString().toLowerCase();
      return (lookupName + lookupVersion)
    },
    getDetail: function(name, version) {
      const lookupName = name.toString().toLowerCase();
      const lookupVersion = version.toString().toLowerCase();
      return this.scheme_details[lookupName][lookupVersion]
    },
    loadSchemeDetails: function (schemes) {
      schemes.forEach(scheme => {
        this.$set(this.scheme_details, scheme.name.toLowerCase(), {});
        scheme.versions.forEach(v => {
          const url = v.repository.replace('github.com', 'raw.githubusercontent.com') + '/info.yaml';
          fetch(url).then(async response => {
            if (response.status === 200) {
              const result = yaml.load(await response.text());
              this.$set(this.scheme_details[scheme.name.toLowerCase()], v.version.toLowerCase(), result);
              const key = this.dialogKey(scheme.name, v.version);
              this.$set(this.dialog[key], false);
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

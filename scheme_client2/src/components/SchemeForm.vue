<template>
  <v-row>
    <v-form v-model="valid">
      <v-jsf :schema="schema" v-model="model" @change="changeModel" :options="options"/>
      <template v-if="!model.bed_url">
        <v-subheader>If you do not yet have a BED file of your primer scheme, you can upload one here</v-subheader>
        <v-file-input label="Primer Scheme Description file (BED)"
                      accept=".bed,.csv,.tsv,text/x-bed,text/csv,text/tab-separated-values"
                      v-model="bed_file"
                      @change="fileReady" ref="bed_file"
      />
      </template>
      <template v-if="!model.reference_url">
        <v-subheader>If you do not provide an URL for the reference sequence FASTA file, select a FASTA file to upload here</v-subheader>
        <v-file-input label="Reference Sequence (FASTA)"
                      accept=".fasta,.fa"
                      v-model="reference_file"
                      @change="fileReady" ref="reference_file"
        />
      </template>
      <v-btn color="primary" @click="submitForm">Add</v-btn>
    </v-form>
  </v-row>
</template>

<script>
import VJsf from '@koumoul/vjsf/lib/VJsf.js'
import '@koumoul/vjsf/lib/VJsf.css'
import '@koumoul/vjsf/lib/deps/third-party.js'

export default {
  name: "SchemeForm",
  data: () => ({
    valid: false,
    model: {
      developers: []
    },
    reference_file: null,
    bed_file: null,
    schema: require('@/assets/schemes-schema.json'),
    options: {
      useValidator: true
    }
  }),
  components: {
    VJsf
  },
  methods: {
    changeModel() {
      this.$emit("changeModel", this.model);
    },
    fileReady() {
      console.log("got a file: bed: " + this.bed_file)
    },
    submitForm() {
      fetch(`http://localhost:8000/schema/${this. model.name}`,{
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.model)
      })
    }
  }
}
</script>

<style scoped>

</style>

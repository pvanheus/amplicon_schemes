<template>
  <pre v-if="Object.keys(data).length">
{{yamlText}}
  </pre>
</template>

<script>
const yaml = require('js-yaml');

export default {
  name: "YamlDisplay",
  props: {
    data: Object
  },
  computed: {
    yamlText() {
      return yaml.dump(this.data)
    }
  }
}
</script>

<style scoped>

</style>

<template>
  <v-container>
    <v-row>
      <v-col>
        <SchemeForm @changeModel="modelChange($event)"/>
      </v-col>
      <v-col>
        <YamlDisplay :data="model"/>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import SchemeForm from "@/components/SchemeForm";
import YamlDisplay from "@/components/YamlDisplay";

export default {
  name: "SchemeSubmit",
  components: {
    SchemeForm,
    YamlDisplay
  },
  data: () => ({
    model: {}
  }),
  methods: {
    modelChange(e) {
      this.model = e;
    }
  }
}
</script>

<style scoped>

</style>

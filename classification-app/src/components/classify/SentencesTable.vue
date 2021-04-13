<template>
  <div>
    <b-table :items="sentences" :fields="fields" striped responsive="sm">

      <template #cell(label_selector)="sentence">
        <LabelSelector v-bind:sentence="sentence.item"/>
      </template>

    </b-table>
  </div>
</template>

<script>
    import LabelSelector from './LabelSelector.vue'

    export default {
        name: "SentencesTable",
        props: ['sentences'],
        components: {
            LabelSelector
        },
        data() {
            return {
                fields: ['sentence', 'label_selector'],
            }
        }
  }
</script>
<template>
  <div>
    <b-table v-if="showTable === true" :items="sentences" :fields="fields" striped responsive="sm">

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
        props: ['sentences', 'showTable'],
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
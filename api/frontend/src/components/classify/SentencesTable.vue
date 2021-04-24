<template>
    <div>
        <b-table v-show="tableShown" :items="sentences" :fields="fields" striped responsive="sm">

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
        props: ['sentences', 'tableShown'],
        components: {
            LabelSelector
        },
        methods: {
          show(tableShown) {
            console.log("Salut fdp")
            console.log(tableShown)
            this.tableShown = tableShown
          }
        },
        data() {
            return {
                fields: ['sentence_text', 'label_selector'],
            }
        }
  }
</script>
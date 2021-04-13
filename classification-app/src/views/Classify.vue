<template>
  <div>
    <h1> Classification page </h1>
    <GetArticleToClassify v-bind:showTable="showTable"/>
    <SentencesTable v-bind:sentences="sentences" v-bind:showTable="showTable"/>
    <SubmitArticle v-bind:sentences="sentences" v-bind:showTable="showTable"/>
  </div>
</template>


<script>
    import GetArticleToClassify from '../components/classify/GetArticleToClassify'
    import SentencesTable from '../components/classify/SentencesTable.vue'
    import SubmitArticle from '../components/classify/SubmitArticle.vue'

    export default {
        name: 'Classify',
        components: {
            GetArticleToClassify,
            SentencesTable,
            SubmitArticle
        },
        data() {
            return {
                fields: ['sentence', 'label_selector'],
                showTable: true,
                sentences: [
                    { id: 1, label: 0, sentence: "On teste des phrases en dur à classifier" },
                    { id: 2, label: 1, sentence: "J'espère que ça va bien marcher avec des phrases longues" },
                    { id: 3, label: 2, sentence: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce at viverra mi, in rhoncus lorem. Phasellus hendrerit orci ut mi congue, sagittis aliquet diam interdum. Mauris ut massa sit amet neque interdum efficitur vestibulum quis lectus. Phasellus vehicula ultricies ipsum, at vestibulum ipsum semper in. Vestibulum at massa lacinia, vestibulum lacus in, sodales ante. Sed ligula libero, scelerisque non lorem non, feugiat tincidunt quam. Proin consequat porttitor vehicula. ' },
                    { id: 4, label: 0, sentence: "C'est pas si mal avec des phrases longues" }
                ]
            }
        }
    }
</script>
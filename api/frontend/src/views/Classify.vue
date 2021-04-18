<template>
  <div>
    <h1> Classification page </h1>
    <GetArticleToClassify v-bind:showTable="showTable" @gotArticle="gotArticle"/>
    <SentencesTable v-bind:sentences="sentences" v-bind:tableShown="tableShown" ref="sentencesTable"/>
    <SubmitArticle v-bind:sentences="sentences" v-bind:tableShown="tableShown" @submitArticle="submitArticle" ref="submitArticle"/>
  </div>
</template>


<script>
    import axios from 'axios' 
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
        methods: {
            gotArticle(params) {
                this.tableShown = params.tableShown
                params.sentences.forEach(function (element) {
                    element.label = -1;
                });
                this.sentences = params.sentences
                console.log("gotArticle")
                console.log(this.tableShown)
                console.log(this.sentences)

                // this.$refs.sentencesTable.show(this.tableShown);
                // this.$refs.submitArticle.show(this.tableShown);
            },
            submitArticle(params) {
                this.tableShown = params.tableShown
                this.sentences = params.sentences

                console.log("submitArticle")
                console.log(this.tableShown)
                console.log(this.sentences)

                this.$refs.sentencesTable.show(this.tableShown);
                this.$refs.submitArticle.show(this.tableShown);
            }
        },
        data() {
            return {
                fields: ['sentence', 'label_selector'],
                token: localStorage.getItem('token') || null,
                sentences: null,
                tableShown: false
            }
        }
    }
</script>
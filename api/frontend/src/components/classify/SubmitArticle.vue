<template>
    <div>
        <b-button @click="onSubmit" v-show="tableShown" type="submit" variant="primary">Submit classification</b-button>
        <SuccessAlert v-bind:message="errorMessage" ref="errorAlert"></SuccessAlert>
    </div>
</template>

<script>
    import axios from 'axios'
    import SuccessAlert from '../generic/SuccessAlert'

    export default {
        name: "SubmitArticle",
        props: ['sentences', 'tableShown'],
        components: {
            SuccessAlert
        },
        data() {
            return {
                errorMessage: "Article successfully classified"
            }
        },
        methods: {
            show(showTable) {
                this.tableShown = showTable
            },
            onSubmit(event) {
                event.preventDefault()
                let sentences_to_submit = this.sentences
                sentences_to_submit.forEach(s => delete s.sentence_text);

                var postData = {
                    sentences: sentences_to_submit,
                };
                let axiosConfig = {
                    headers: {
                        Authorization: 'Token ' + localStorage.getItem('token')
                    }
                };

                axios.post('article/classify', postData, axiosConfig
                ).then(response => {
                    console.log(response)
                    this.$emit("submitArticle", {
                        tableShown: false,
                        sentences: null
                    })
                    this.$refs.errorAlert.showAlert();
                }).catch(error => {
                    console.log(error)
                })
            }
        },
    }
</script>
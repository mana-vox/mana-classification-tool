<template>
    <div>
        <b-button @click="onSubmit" type="submit" variant="primary">Get a new article</b-button>
        <ErrorAlert v-bind:message="errorMessage" ref="errorAlert"></ErrorAlert>
    </div>
</template>

<script>
    import axios from 'axios' 
    import ErrorAlert from '../generic/ErrorAlert'

    export default {
        name: "GetArticleToClassify",
        components: {
            ErrorAlert
        },
        props: ['showTable'],
        data() {
            return {
                errorMessage: "You have no more articles to classify"
            }
        },
        methods: {
            onSubmit(event) {
                event.preventDefault()

                axios.get('article/get', {
                    headers: {
                        Authorization: 'Token ' + localStorage.getItem('token')
                    }
                }).then(response => {
                    console.log(response)
                    this.$emit("gotArticle", {
                        tableShown: true,
                        sentences: response.data.sentences
                    })
                }).catch(error => {
                    console.log(error)
                    this.$refs.errorAlert.showAlert();
                })
            }
        }
    }
</script>
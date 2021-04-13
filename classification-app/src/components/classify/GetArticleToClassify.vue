<template>
    <div>
        <b-button @click="onSubmit" type="submit" variant="primary">Get a new article</b-button>
    </div>
</template>

<script>
    export default {
        name: "GetArticleToClassify",
        props: ['showTable'], 
        methods: {
            onSubmit(event) {
                event.preventDefault()
                this.showTable = true
                alert(JSON.stringify("Get article to classify"))
            }
        }
    }
</script>
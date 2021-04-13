<template>
    <div>
        <b-button @click="onSubmit" type="submit" variant="primary">Submit classification</b-button>
    </div>
</template>

<script>
    export default {
        name: "SubmitArticle",
        props: ['sentences'],
        methods: {
            onSubmit(event) {
                event.preventDefault()
                alert(JSON.stringify(this.sentences))
            }
        }
    }
</script>
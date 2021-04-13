<template>
    <div>
        <b-button @click="onSubmit" type="submit" variant="primary">Submit classification</b-button>
    </div>
</template>

<script>
    export default {
        name: "SubmitArticle",
        props: ['sentences', 'showTable'],
        methods: {
            onSubmit(event) {
                event.preventDefault()
                this.showTable = false
                alert(JSON.stringify(this.sentences))
            }
        }
    }
</script>
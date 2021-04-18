<template>
    <div>
        <b-alert
            :show="dismissCountDown"
            dismissible
            fade
            variant="danger"
            @dismiss-count-down="countDownChanged"
            >
            {{ message }}
        </b-alert>
    </div>
</template>

<script>
    export default {
        name: "ErrorAlert",
        props: ['message'],
        data() {
            return {
                dismissSecs: 5,
                dismissCountDown: 0,
            }
        },
        methods: {
            countDownChanged(dismissCountDown) {
                this.dismissCountDown = dismissCountDown
            },
            showAlert() {
                this.dismissCountDown = this.dismissSecs
            },
        }
    }
</script>
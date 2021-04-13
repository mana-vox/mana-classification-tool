<template>
    <div>
        <b-button variant='primary' v-b-modal.sign-up-modal>Sign up</b-button>

        <b-modal @ok="onSubmit" id="sign-up-modal" title="Sign up">
            <LoginForm v-bind:login_form="login_form"></LoginForm>
        </b-modal>

    </div>
</template>

<script>
    import LoginForm from './LoginForm.vue'

    export default {
        name: "SignUp",
        components: {
            LoginForm
        },
        data() {
            return {
                login_form: {
                    login: '',
                    password: '',
                },
            }
        },
        methods: {
            onSubmit(event) {
                event.preventDefault()
                alert(JSON.stringify(this.login_form))
                this.$nextTick(() => {
                    this.$bvModal.hide('sign-up-modal')
                })
            },
        }
    }
</script>
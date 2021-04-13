<template>
    <div>
        <b-form @submit="onSubmit" @reset="onReset">
            <LoginForm v-bind:login_form="login_form"></LoginForm>
            <b-button type="submit" variant="primary">Submit</b-button>
            <b-button type="reset" variant="danger">Reset</b-button>
        </b-form>
    </div>
</template>

<script>
    import LoginForm from './LoginForm.vue'

    export default {
        name: "Login",
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
            },
            onReset(event) {
                event.preventDefault()
                this.login_form.login = ''
                this.login_form.password = ''
            }
        }
    }
</script>
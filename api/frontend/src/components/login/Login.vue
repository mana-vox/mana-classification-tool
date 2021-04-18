<template>
    <div>
        <b-form @submit="onSubmit" @reset="onReset">
            <LoginForm v-bind:login_form="login_form"></LoginForm>
            <ErrorAlert v-bind:message="errorMessage" ref="errorAlert"></ErrorAlert>
            <b-button type="submit" variant="primary">Submit</b-button>
            <b-button type="reset" variant="danger">Reset</b-button>
        </b-form>
    </div>
</template>

<script>
    import axios from 'axios'
    import LoginForm from './LoginForm.vue'
    import ErrorAlert from '../generic/ErrorAlert'
    import { bus } from '../../main'

    export default {
        name: "Login",
        components: {
            LoginForm, ErrorAlert
        },
        data() {
            return {
                login_form: {
                    login: '',
                    password: '',
                },
                token: null,
                errorMessage: "Failed (bad login and/or password)"
            }
        },
        methods: {
            onSubmit(event) {
                event.preventDefault()
                axios.post('account/login', {
                    "email": this.login_form.login,
                    "username": this.login_form.login,
                    "password": this.login_form.password
                }).then(response => {
                    localStorage.setItem('token', response.data.token)
                    bus.$emit('logged', 'User logged')
                    this.$router.push("/classify")
                }).catch(error => {
                    localStorage.removeItem('token')
                    this.$refs.errorAlert.showAlert();
                    console.log(error.response)
                })
            },
            onReset(event) {
                event.preventDefault()
                this.login_form.login = ''
                this.login_form.password = ''
            }
        }
    }
</script>
<template>
    <div>
        <b-button @click="modalShow=true" variant='primary' v-b-modal.sign-up-modal>Sign up</b-button>

        <b-modal @ok="onSubmit" v-if="modalShow" id="sign-up-modal" title="Sign up">
            <LoginForm v-bind:login_form="login_form"></LoginForm>
            <ErrorAlert v-bind:message="errorMessage" ref="errorAlert"></ErrorAlert>
        </b-modal>

    </div>
</template>

<script>
    import axios from 'axios'
    import LoginForm from './LoginForm.vue'
    import ErrorAlert from '../generic/ErrorAlert'

    export default {
        name: "SignUp",
        components: {
            LoginForm, ErrorAlert
        },
        data() {
            return {
                login_form: {
                    login: '',
                    password: '',
                },
                errorMessage: "Unable to create user. Username already exists.",
                modalShow: false
            }
        },
        methods: {
            onSubmit(event) {
                event.preventDefault()
                axios.post('account/register', {
                        "email": this.login_form.login,
                        "password": this.login_form.password
                    }).then(response => {
                        this.modalShow = false
                        console.log(response)
                    }).catch(error => {
                        this.$refs.errorAlert.showAlert();
                        console.log(error)
                    })
            },
        }
    }
</script>
<template>
    <div>
        <b-form-group
            id="input-group-1"
            label="Login:"
            label-for="input-1"
        >
            <b-form-input
                id="input-1"
                v-model="login_form.login"
                type="text"
                placeholder="Enter login"
                required></b-form-input>
        </b-form-group>
        <b-form-group
            id="input-group-2"
            label="Password:"
            label-for="input-2"
        >
            <b-form-input
                id="input-2"
                v-model="login_form.password"
                type="password"
                placeholder="Enter password"
                required></b-form-input>
        </b-form-group>
    </div>
</template>

<script>
    export default {
        name: "LoginForm",
        props: ['login_form']
    }
</script>
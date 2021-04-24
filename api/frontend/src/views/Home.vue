<template>
    <div class="home">
        <h1> Welcome to MANA classification tool </h1>
        <h2> Please login or sign up </h2>
        <Login/>
        <SignUp/>
    </div>
</template>

<script>
import Login from '../components/login/Login.vue'
import SignUp from '../components/login/SignUp.vue'

export default {
    name: 'Home',
        async created() {
        localStorage.removeItem("token")
    },
        components: {
        Login,
        SignUp
    }
}
</script>

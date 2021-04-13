<template>
  <div id="app">
    <h1> Hello la Team MANA </h1>
    <Login/>
    <SignUp/>
  </div>
</template>

<script>
import Login from './components/login/Login.vue'
import SignUp from './components/login/SignUp.vue'

export default {
  name: 'App',
  components: {
    Login, SignUp
  }
}
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  padding-left: 50px;
  padding-right: 50px;
  // text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

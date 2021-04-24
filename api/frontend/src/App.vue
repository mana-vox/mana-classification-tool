<template>
    <div>
        <div>
            <b-navbar toggleable="lg" type="dark" variant="info">
                <b-navbar-brand to="/">MANA</b-navbar-brand>

                <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

                <b-collapse id="nav-collapse" is-nav>

                    <!-- Right aligned nav items -->
                    <b-navbar-nav class="ml-auto">
                    
                        <!-- <router-link to="/about">About</router-link> -->
                        <b-nav-item to="/about">About</b-nav-item>

                        <b-nav-item-dropdown right v-if="isLogged">
                            <!-- Using 'button-content' slot -->
                            <template #button-content>
                                <em>User</em>
                            </template>
                            <b-dropdown-item @click="logout">Sign Out</b-dropdown-item>
                        </b-nav-item-dropdown>
                    </b-navbar-nav>
                </b-collapse>
            </b-navbar>
        </div>
        <div id='app'>
            <router-view/>
        </div>
    </div>
</template>

<script>
    import { bus } from './main'

    export default {
        name: "App",
        data() {
            return {
                isLogged: checkIfIsLogged()
            }
        },
        created() {
            bus.$on('logged', () => {
                this.isLogged = this.checkIfIsLogged()
            })
        },
        methods: {
            checkIfIsLogged() {
                if (localStorage.getItem("token")) {
                  return true
                } else {
                  return false
                }
            },
            logout() {
                localStorage.removeItem("token")
                bus.$emit('logged', 'User logged out')
                this.$router.push("/")
            }
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
    color: #2c3e50;
}

</style>
<template>
  <div>
    <vs-input
        v-validate="'required'"
        data-vv-validate-on="blur"
        name="email"
        icon-no-border
        icon="icon icon-user"
        icon-pack="feather"
        label-placeholder="Email"
        v-model="email"
        class="w-full"/>
    <span class="text-danger text-sm">{{ errors.first('email') }}</span>

    <vs-input
        data-vv-validate-on="blur"
        v-validate="'required|min:6|max:10'"
        type="password"
        name="password"
        icon-no-border
        icon="icon icon-lock"
        icon-pack="feather"
        label-placeholder="Password"
        v-model="password"
        class="w-full mt-6" />
    <span class="text-danger text-sm">{{ errors.first('password') }}</span>

    <div class="flex flex-wrap justify-between my-5">
        <vs-checkbox v-model="checkbox_remember_me" class="mb-3">Remember Me</vs-checkbox>
        <router-link to="/pages/forgot-password">Forgot Password?</router-link>
    </div>
    <div class="flex flex-wrap justify-between mb-3">
      <vs-button  type="border" @click="registerUser">Register</vs-button>
      <vs-button :disabled="!validateForm" @click="loginJWT">Login</vs-button>
    </div>
  </div>
</template>

<script>
import UsersService from '@/services/UserService'
export default {
  data() {
    return {
      email: 'admin',
      password: 'admin',
      checkbox_remember_me: false
    }
  },
  computed: {
    validateForm() {
      return !this.errors.any() && this.email != '' && this.password != '';
    },
  },
  methods: {
    checkLogin() {
      // If user is already logged in notify
      if (this.$store.state.auth.isUserLoggedIn()) {

        // Close animation if passed as payload
        // this.$vs.loading.close()

        this.$vs.notify({
          title: 'Login Attempt',
          text: 'You are already logged in!',
          iconPack: 'feather',
          icon: 'icon-alert-circle',
          color: 'warning'
        })

        return false
      }
      return true
    },
    loginJWT() {
      let vm = this
      vm.loading = true

      UsersService.login({
        username: vm.email,
        password: vm.password
      })
        .then(function (response) {
          if (response.data) {
            vm.$store.dispatch('authentication/login', true)
            vm.$store.dispatch('authentication/setAutentificacionR', {tokenRe: response.data.refresh,})
            vm.$store.dispatch('user/userLogged', new Boolean(true))
            vm.$store.dispatch('user/setPermissions', response.data.permissions)
            vm.$store.dispatch('authentication/setAuthentication', {token: response.data.access,})
            vm.$router.push({ name: 'dashboard' })
          }
          // eslint-disable-next-line handle-callback-err
        })
        .catch(function () {
          vm.$vs.notify({
            title: 'Error al iniciar sesión',
            text: 'Usuario y/o contraseña invalidos',
            color: 'danger'
          })
        })
    },
    registerUser() {
      if (!this.checkLogin()) return
      this.$router.push('/pages/register').catch(() => {})
    }
  }
}

</script>


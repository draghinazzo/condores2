const auth = {
  namespaced: true,
  state: {
    isAuthenticated: false,
    authentication: [],
    authenticationR: [],
  },
  mutations: {
    isAuthenticated(state, payload) {
      state.isAuthenticated = payload
    },
    authentication(state, payload) {
      state.authentication = payload
    },
    authenticationR(state, payload) {
      state.authenticationR = payload
    },
  },
  actions: {
    login({ commit }, payload) {
      commit('isAuthenticated', payload)
    },
    setAuthentication({ commit }, payload) {
      commit('authentication', payload)
    },
    setAutentificacionR({ commit }, payload) {
      commit('authenticationR', payload)
    },
    logout({ commit }) {
      commit('isAuthenticated', false)
      commit('authentication', [])
    },
  },
  getters: {
    isAuthenticated(state) {
      return state.isAuthenticated
    },
  },
}

export default auth
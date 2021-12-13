// import CatalogosService from '@/services/CatalogosService'

const user = {
  namespaced: true,
  state: {
    data: '',
    userLogged: false,
    profile: '',
    assigned: 0,
    permissions: [],
    sectores_hijos: [],
  },
  mutations: {
    allUsers(state, payload) {
      state.users = payload
    },
    userLogged(state, payload) {
      state.data = payload
      state.userLogged = true
    },
    setPermissions(state, payload) {
      state.permissions = payload
    },
    setProfile(state, payload) {
      state.profile = payload
    },
    setAssigned(state, payload) {
      state.assigned = payload
    },
    logout(state) {
      state.token = ''
      state.data = ''
      state.userLogged = false
      state.profile = ''
      state.assigned = 0
      state.permissions = []
      state.sectores_hijos = []
    },
  },
  actions: {
    userLogged({ commit }, payload) {
      commit('userLogged', payload)
    },
    setPermissions({ commit }, payload) {
      commit('setPermissions', payload)
    },
    setProfile({ commit }, payload) {
      commit('setProfile', payload)
    },
    setAssigned({ commit }, payload) {
      commit('setAssigned', payload)
    },
    allUsers({ commit }, payload) {
      commit('allUsers', payload)
    },
    deleteUser({ commit }, payload) {
      commit('deleteUser', payload)
    },
    logout({ commit }) {
      commit('logout')
    },
    setAdscripcionesHijas({ commit }, payload) {
      commit('setAdscripcionesHijas', payload)
    },
    /*
    setSectoresHijos({ commit }, payload) {
      CatalogosService.getAllChildren(payload).then(response => {
        commit('setSectoresHijos', response.data)
      })
    },
    setSectores({ commit }) {
      CatalogosService.getAllAdscripcion().then(response => {
        commit('setSectores', response.data)
      })
    },
    */
  },
  getters: {
    userPermissions: state => ({ permissions: state.permissions, data: state.data }),
    user: state => state.data,
    
  },
}

export default user

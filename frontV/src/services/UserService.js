import Api from '@/services/Api'
const resource = 'user'

export default {
  logout () {
    return Api().get('logout')
      .catch((error) => {
        if (error.response) {
          // console.log(JSON.stringify(error.response))
          alert(JSON.stringify(error.response.data))
        } else if (error.request) {
          console.log(error.request)
        } else {
          console.log('Error', error.message)
        }
      })
  },
  fetchUsers () {
    return Api().get('driver')
      .catch((error) => {
        if (error.response) {
          console.log(error.response)
          alert(error.response.data)
        } else if (error.request) {
          console.log(error.request)
        } else {
          console.log('Error', error.message)
        }
      })
  },
  getIniciales (params) {
    return Api().post('getIniciales', params)
  },
  login (params) {
    console.log('dsdsd', params)
    return Api().post('tokenC', params)
  },
  updateUser  (params) {
    return Api().put('user/' + params.id, params)
      .catch((error) => {
        if (error.response) {
          console.log(error.response)
        } else if (error.request) {
          console.log(error.request)
        } else {
          console.log('Error', error.message)
        }
      })
  },
  getUser  (params) {
    return Api().get('user/' + params.id)
      .catch((error) => {
        if (error.response) {
          console.log(error.response)
        } else if (error.request) {
          console.log(error.request)
        } else {
          console.log('Error', error.message)
        }
      })
  },
  deleteUser (id) {
    return Api().delete('user/' + id)
      .catch((error) => {
        if (error.response) {
          console.log(error.response)
        } else if (error.request) {
          console.log(error.request)
        } else {
          console.log('Error', error.message)
        }
      })
  },
  create (form) {
    return Api().post(resource, form)
  },
  getRoles  () {
    return Api().get('roles')
  },
  getById (id) {
    return Api().get(`${resource}/${id}`)
  },
  update (id, form) {
    return Api().put(`${resource}/${id}`, form)
  },
  fetchList (listQuery) {
    return Api().get(resource, {
      params: {
        pageSize: listQuery.limit,
        page: listQuery.page,
        sort: listQuery.sortBy,
        order: listQuery.sortDesc,
        query: listQuery.query
      }
    })
  }
}

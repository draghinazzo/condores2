/* eslint-disable no-underscore-dangle */
/* eslint-disable no-param-reassign */
/* eslint-disable no-unused-vars */
/* eslint-disable no-prototype-builtins */
import axios from 'axios'
import store from '@/store/store.js'

const instance = axios.create({
  //baseURL: `http://10.13.123.8:8000/api`
  baseURL: `http://192.168.1.131:8000/api`

  // baseURL: `http://${process.env.VUE_APP_BASE_URL}`,
  // baseURL: `http://${process.env.VUE_APP_BASE_URL}/api/v1`,
})

instance.interceptors.request.use((config, next) => {
  if (localStorage.hasOwnProperty('plataforma-condores') && JSON.parse(localStorage.getItem('plataforma-condores')).authentication.authentication.token) {
    config.headers.Authorization = [
      'Bearer', JSON.parse(localStorage.getItem('plataforma-condores')).authentication.authentication.token,
    ].join(' ')
  } else {
    delete config.headers.Authorization
  }
  return config
}, error => Promise.reject(error))

instance.interceptors.response.use(response => response, error => {
  const originalRequest = error.config
  // TODO ADD REFRESH TOKEN METHOD
  if (error.response && error.response.status === 401 && !originalRequest._retry) {
    originalRequest._retry = true
    const authUser = JSON.parse(window.localStorage.getItem('plataforma-condores'))
    const rToken = authUser.authentication.authenticationR.tokenRe

    return axios.post(`http://localhost:8000/api/token/refresh2`,{"refresh": rToken})
    .then(({ data }) => {
      store.dispatch('authentication/setAuthentication', {token: data.access,})
      axios.defaults.headers.common.Authorization = `Bearer ${data.access}`
      originalRequest.headers.Authorization = `Bearer ${data.access}`
      return axios(originalRequest)
    })
  }
  return Promise.reject(error)
})

export default () => instance

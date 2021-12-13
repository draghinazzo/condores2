import Api from '@/services/Api'

export default {
  obtener(params) {
    return Api().get(`/misiones/helicoptero/?limit=${params.limit}&offset=${params.offset}&nombre=${params.nombre}`)
  },
  crear(params) {
    return Api().post(`/misiones/helicoptero/`, params)
  },
  eliminar(id) {
    return Api().delete(`/misiones/helicoptero/${id}`, )
  },
  obtenerId(id) {
    return Api().get(`/misiones/helicoptero/${id}`, )
  },
  actualizarId(id, params) {
    return Api().put(`/misiones/helicoptero/${id}/`, params)
  },
  select(params) {
    return Api().get(`/misiones/helicopteroSelect/?limit=${params.limit}&offset=${params.offset}&nombre=${params.nombre}`)
  },

}

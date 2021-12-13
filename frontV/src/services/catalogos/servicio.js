import Api from '@/services/Api'

export default {
  obtener(params) {
    return Api().get(`/misiones/servicio/?limit=${params.limit}&offset=${params.offset}&nombre=${params.nombre}`)
  },
  crear(params) {
    return Api().post(`/misiones/servicio/`, params)
  },
  eliminar(id) {
    return Api().delete(`/misiones/servicio/${id}`, )
  },
  obtenerId(id) {
    return Api().get(`/misiones/servicio/${id}`, )
  },
  actualizarId(id, params) {
    return Api().put(`/misiones/servicio/${id}/`, params)
  },

}

import Api from '@/services/Api'

export default {
  obtener(params) {
    return Api().get(`/misiones/misiones/?limit=${params.limit}&offset=${params.offset}&nombre=${params.nombre}`)
  },
  crear(params) {
    return Api().post(`/misiones/misiones/`, params)
  },
  eliminar(id) {
    return Api().delete(`/misiones/misiones/${id}`, )
  },
  obtenerId(id) {
    return Api().get(`/misiones/misiones/${id}`, )
  },
  actualizarId(id, params) {
    return Api().put(`/misiones/misiones/${id}/`, params)
  },

}

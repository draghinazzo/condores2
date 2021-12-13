import Api from '@/services/Api'

export default {
  obtener(params) {
    return Api().get(`/misiones/cargo/?limit=${params.limit}&offset=${params.offset}&nombre=${params.nombre}`)
  },
  crear(params) {
    return Api().post(`/misiones/cargo/`, params)
  },
  eliminar(id) {
    return Api().delete(`/misiones/cargo/${id}`, )
  },
  obtenerId(id) {
    return Api().get(`/misiones/cargo/${id}`, )
  },
  actualizarId(id, params) {
    return Api().put(`/misiones/cargo/${id}/`, params)
  },

}

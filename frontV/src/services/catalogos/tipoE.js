import Api from '@/services/Api'

export default {
  obtener(params) {
    return Api().get(`/misiones/tipoE/?limit=${params.limit}&offset=${params.offset}&nombre=${params.nombre}`)
  },
  crear(params) {
    return Api().post(`/misiones/tipoE/`, params)
  },
  eliminar(id) {
    return Api().delete(`/misiones/tipoE/${id}`, )
  },
  obtenerId(id) {
    return Api().get(`/misiones/tipoE/${id}`, )
  },
  actualizarId(id, params) {
    return Api().put(`/misiones/tipoE/${id}/`, params)
  },

}

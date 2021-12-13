import Api from '@/services/Api'

export default {
  obtener(params) {
    return Api().get(`/tipoE/direccionM/?limit=${params.limit}&offset=${params.offset}&nombre=${params.nombre}`)
  },
  crear(params) {
    return Api().post(`/tipoE/direccionM/`, params)
  },
  eliminar(id) {
    return Api().delete(`/tipoE/direccionM/${id}`, )
  },
  obtenerId(id) {
    return Api().get(`/tipoE/direccionM/${id}`, )
  },
  actualizarId(id, params) {
    return Api().put(`/tipoE/direccionM/${id}/`, params)
  },
  
  select(params) {
    return Api().get(`/misiones/tipoESelect/?limit=${params.limit}&offset=${params.offset}&nombre=${params.nombre}`)
  },

}

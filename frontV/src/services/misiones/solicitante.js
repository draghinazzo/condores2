import Api from '@/services/Api'

export default {
  obtener(params) {
    return Api().get(`/solicitante/direccionM/?limit=${params.limit}&offset=${params.offset}&nombre=${params.nombre}`)
  },
  crear(params) {
    return Api().post(`/solicitante/direccionM/`, params)
  },
  eliminar(id) {
    return Api().delete(`/solicitante/direccionM/${id}`, )
  },
  obtenerId(id) {
    return Api().get(`/solicitante/direccionM/${id}`, )
  },
  actualizarId(id, params) {
    return Api().put(`/solicitante/direccionM/${id}/`, params)
  },
  
  select(params) {
    return Api().get(`/misiones/solicitanteSelect/?limit=${params.limit}&offset=${params.offset}&nombre=${params.nombre}`)
  },

}

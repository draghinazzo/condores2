import Api from '@/services/Api'

export default {
  obtener(params) {
    return Api().get(`/misiones/direccionM/?limit=${params.limit}&offset=${params.offset}&nombre=${params.nombre}`)
  },
  crear(params) {
    return Api().post(`/misiones/direccionM/`, params)
  },
  eliminar(id) {
    return Api().delete(`/misiones/direccionM/${id}`, )
  },
  obtenerId(id) {
    return Api().get(`/misiones/direccionM/${id}`, )
  },
  actualizarId(id, params) {
    return Api().put(`/misiones/direccionM/${id}/`, params)
  },
  
  select(params) {
    return Api().get(`/misiones/direccionMSelect/?limit=${params.limit}&offset=${params.offset}&nombre=${params.nombre}`)
  },

}

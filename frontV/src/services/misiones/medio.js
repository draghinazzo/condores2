import Api from '@/services/Api'

export default {
  obtener(params) {
    return Api().get(`/medio/direccionM/?limit=${params.limit}&offset=${params.offset}&nombre=${params.nombre}`)
  },
  crear(params) {
    return Api().post(`/medio/direccionM/`, params)
  },
  eliminar(id) {
    return Api().delete(`/medio/direccionM/${id}`, )
  },
  obtenerId(id) {
    return Api().get(`/medio/direccionM/${id}`, )
  },
  actualizarId(id, params) {
    return Api().put(`/medio/direccionM/${id}/`, params)
  },
  
  select(params) {
    return Api().get(`/misiones/medioSelect/?limit=${params.limit}&offset=${params.offset}&nombre=${params.nombre}`)
  },

}

import Api from '@/services/Api'

export default {
  obtener(params) {
    return Api().get(`/servicio/direccionM/?limit=${params.limit}&offset=${params.offset}&nombre=${params.nombre}`)
  },
  crear(params) {
    return Api().post(`/servicio/direccionM/`, params)
  },
  eliminar(id) {
    return Api().delete(`/servicio/direccionM/${id}`, )
  },
  obtenerId(id) {
    return Api().get(`/servicio/direccionM/${id}`, )
  },
  actualizarId(id, params) {
    return Api().put(`/servicio/direccionM/${id}/`, params)
  },
  
  select(params) {
    return Api().get(`/misiones/servicioSelect/?limit=${params.limit}&offset=${params.offset}&nombre=${params.nombre}`)
  },

}

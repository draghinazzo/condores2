import Api from '@/services/Api'

export default {
  obtener(params) {
    return Api().get(`/sexo/direccionM/?limit=${params.limit}&offset=${params.offset}&nombre=${params.nombre}`)
  },
  crear(params) {
    return Api().post(`/sexo/direccionM/`, params)
  },
  eliminar(id) {
    return Api().delete(`/sexo/direccionM/${id}`, )
  },
  obtenerId(id) {
    return Api().get(`/sexo/direccionM/${id}`, )
  },
  actualizarId(id, params) {
    return Api().put(`/sexo/direccionM/${id}/`, params)
  },
  
  select(params) {
    return Api().get(`/misiones/sexoSelect/?limit=${params.limit}&offset=${params.offset}&nombre=${params.nombre}`)
  },

}

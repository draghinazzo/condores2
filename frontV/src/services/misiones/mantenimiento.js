import Api from '@/services/Api'

export default {
  obtener(params) {
    return Api().get(`/misiones/mantenimiento/?limit=${params.limit}&offset=${params.offset}&nombre=${params.nombre}`)
  },
  crear(params) {
    return Api().post(`/misiones/mantenimiento/`, params)
  },
  eliminar(id) {
    return Api().delete(`/misiones/mantenimiento/${id}`, )
  },
  obtenerId(id) {
    return Api().get(`/misiones/mantenimiento/${id}`, )
  },
  actualizarId(id, params) {
    return Api().put(`/misiones/mantenimiento/${id}/`, params)
  },

}

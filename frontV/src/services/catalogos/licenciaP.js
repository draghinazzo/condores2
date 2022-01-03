import Api from '@/services/Api'

export default {
  obtener(params) {
    return Api().get(`/misiones/licenciaPersona/?limit=${params.limit}&offset=${params.offset}&nombre=${params.nombre}`)
  },
  crear(params) {
    return Api().post(`/misiones/licenciaPersona/`, params)
  },
  eliminar(id) {
    return Api().delete(`/misiones/licenciaPersona/${id}`, )
  },
  obtenerId(id) {
    return Api().get(`/misiones/licenciaPersona/${id}`, )
  },
  actualizarId(id, params) {
    return Api().put(`/misiones/licenciaPersona/${id}/`, params)
  },

}

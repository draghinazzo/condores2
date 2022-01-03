import Api from '@/services/Api'

export default {
  obtener(params) {
    return Api().get(`/misiones/domiciolioPersona/?limit=${params.limit}&offset=${params.offset}&nombre=${params.nombre}`)
  },
  crear(params) {
    return Api().post(`/misiones/domiciolioPersona/`, params)
  },
  eliminar(id) {
    return Api().delete(`/misiones/domiciolioPersona/${id}`, )
  },
  obtenerId(id) {
    return Api().get(`/misiones/domiciolioPersona/${id}`, )
  },
  actualizarId(id, params) {
    return Api().put(`/misiones/domiciolioPersona/${id}/`, params)
  },

}

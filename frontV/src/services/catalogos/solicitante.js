import Api from '@/services/Api'

export default {
  obtener(params) {
    return Api().get(`/misiones/solicitante/?limit=${params.limit}&offset=${params.offset}&nombre=${params.nombre}`)
  },
  crear(params) {
    return Api().post(`/misiones/solicitante/`, params)
  },
  eliminar(id) {
    return Api().delete(`/misiones/solicitante/${id}`, )
  },
  obtenerId(id) {
    return Api().get(`/misiones/solicitante/${id}`, )
  },
  actualizarId(id, params) {
    return Api().put(`/misiones/solicitante/${id}/`, params)
  },

}

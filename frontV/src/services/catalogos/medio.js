import Api from '@/services/Api'

export default {
  obtener(params) {
    return Api().get(`/misiones/medio/?limit=${params.limit}&offset=${params.offset}&nombre=${params.nombre}`)
  },
  crear(params) {
    return Api().post(`/misiones/medio/`, params)
  },
  eliminar(id) {
    return Api().delete(`/misiones/medio/${id}`, )
  },
  obtenerId(id) {
    return Api().get(`/misiones/medio/${id}`, )
  },
  actualizarId(id, params) {
    return Api().put(`/misiones/medio/${id}/`, params)
  },

}

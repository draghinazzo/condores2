import Api from '@/services/Api'

export default {
  obtener(params) {
    return Api().get(`/misiones/persona/?limit=${params.limit}&offset=${params.offset}&numeroEmpleado=${params.nombre}`)
  },
  crear(params) {
    return Api().post(`/misiones/persona/`, params)
  },
  eliminar(id) {
    return Api().delete(`/misiones/persona/${id}`, )
  },
  obtenerId(id) {
    return Api().get(`/misiones/persona/${id}`, )
  },
  actualizarId(id, params) {
    return Api().put(`/misiones/persona/${id}/`, params)
  },
  pagina(params) {
    return Api().get(`/misiones/persona/?page=${params}`)
  },

}

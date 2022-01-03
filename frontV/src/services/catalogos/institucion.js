import Api from '@/services/Api'

export default {
  obtener(params) {
    return Api().get(`/misiones/catInstitucion/?limit=${params.limit}&offset=${params.offset}&nombre=${params.nombre}`)
  },
  crear(params) {
    return Api().post(`/misiones/catInstitucion/`, params)
  },
  eliminar(id) {
    return Api().delete(`/misiones/catInstitucion/${id}`, )
  },
  obtenerId(id) {
    return Api().get(`/misiones/catInstitucion/${id}`, )
  },
  actualizarId(id, params) {
    return Api().put(`/misiones/catInstitucion/${id}/`, params)
  },
  select(params) {
    return Api().get(`/misiones/selectInstitucion/?limit=${params.limit}&offset=${params.offset}&nombre=${params.nombre}`)
  },

}

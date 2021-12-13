import Api from '@/services/Api'

export default {
  obtener(params) {
    return Api().get(`/capacitacion/capacitacion/?limit=${params.limit}&offset=${params.offset}&nombre=${params.nombre}`)
  },
  crear(params) {
    return Api().post(`/capacitacion/capacitacion/`, params)
  },
  eliminar(id) {
    return Api().delete(`/capacitacion/capacitacion/${id}`, )
  },
  obtenerId(id) {
    return Api().get(`/capacitacion/capacitacion/${id}`, )
  },
  actualizarId(id, params) {
    return Api().put(`/capacitacion/capacitacion/${id}/`, params)
  },
  select(params) {
    return Api().get(`/capacitacion/cursoSelect/?limit=${params.limit}&offset=${params.offset}&nombre=${params.nombre}`)
  },

}

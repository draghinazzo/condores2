import Api from '@/services/Api'

export default {
  obtener(params) {
    return Api().get(`/capacitacion/instructor/?limit=${params.limit}&offset=${params.offset}&nombre=${params.nombre}`)
  },
  crear(params) {
    return Api().post(`/capacitacion/instructor/`, params)
  },
  eliminar(id) {
    return Api().delete(`/capacitacion/instructor/${id}`, )
  },
  obtenerId(id) {
    return Api().get(`/capacitacion/instructor/${id}`, )
  },
  actualizarId(id, params) {
    return Api().put(`/capacitacion/instructor/${id}/`, params)
  },

  select(params) {
    return Api().get(`/capacitacion/instructorSelect/?limit=${params.limit}&offset=${params.offset}&nombre=${params.nombre}`)
  },
}

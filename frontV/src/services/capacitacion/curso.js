import Api from '@/services/Api'

export default {
  obtener(params) {
    return Api().get(`/capacitacion/curso/?limit=${params.limit}&offset=${params.offset}&nombre=${params.nombre}`)
  },
  crear(params) {
    return Api().post(`/capacitacion/curso/`, params)
  },
  eliminar(id) {
    return Api().delete(`/capacitacion/curso/${id}`, )
  },
  obtenerId(id) {
    return Api().get(`/capacitacion/curso/${id}`, )
  },
  actualizarId(id, params) {
    return Api().put(`/capacitacion/curso/${id}/`, params)
  },

}

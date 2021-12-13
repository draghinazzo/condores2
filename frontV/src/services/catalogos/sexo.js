import Api from '@/services/Api'

export default {
  obtener(params) {
    return Api().get(`/misiones/sexo/?limit=${params.limit}&offset=${params.offset}&nombre=${params.nombre}`)
  },
  crear(params) {
    return Api().post(`/misiones/sexo/`, params)
  },
  eliminar(id) {
    return Api().delete(`/misiones/sexo/${id}`, )
  },
  obtenerId(id) {
    return Api().get(`/misiones/sexo/${id}`, )
  },
  actualizarId(id, params) {
    return Api().put(`/misiones/sexo/${id}/`, params)
  },

}

import Api from '@/services/Api'

export default {
  consultarEmpleado(placa) {
    return Api().get(`/Consulta/${placa}`, )
  },
}

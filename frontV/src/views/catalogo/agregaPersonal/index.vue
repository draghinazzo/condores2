<template>
    <vx-card title="Agregar personal" id="parentx-demo-5">
    <form>
        <vs-row vs-align="flex-end"
                vs-type="flex" 
                vs-justify="space-between" vs-w="12">

            <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="2">
                <vs-input v-on:blur="consularN" size="large" v-validate="'required'" label="Numero de empleado" placeholder="Numero de empleado" name="Numero de empleado" v-model="form.numeroEmpleado" class="mt-5 w-full" />
                <span class="text-danger text-sm" v-show="errors.has('numeroEmpleado')">{{ errors.first('numeroEmpleado') }}</span>
            </vs-col>  

            <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="2">
                <vs-input size="large" v-validate="'required'" label="Nombre" placeholder="Nombre" name="Nombre" v-model="form.nombre" class="mt-5 w-full" />
                <span class="text-danger text-sm" v-show="errors.has('Nombre')">{{ errors.first('Nombre') }}</span>
            </vs-col>    
            <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="2">
                <vs-input size="large" v-validate="'required'" label="Apellido1" placeholder="Apellido1" name="Apellido1" v-model="form.apellido1" class="mt-5 w-full" />
                <span class="text-danger text-sm" v-show="errors.has('Apellido1')">{{ errors.first('Apellido1') }}</span>
            </vs-col>    
            <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="2">
                <vs-input size="large" v-validate="'required'" label="Apellido2" placeholder="Apellido2" name="Apellido2" v-model="form.apellido2" class="mt-5 w-full" />
                <span class="text-danger text-sm" v-show="errors.has('Apellido2')">{{ errors.first('Apellido2') }}</span>
            </vs-col>
        </vs-row>
        <vs-row vs-align="flex-end"
                vs-type="flex" 
                vs-justify="space-between" vs-w="12">

             <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="2">
                <vs-input size="large" v-validate="'required'" label="CURP" placeholder="CURP" name="CURP" v-model="form.curp" class="mt-5 w-full" />
                <span class="text-danger text-sm" v-show="errors.has('CURP')">{{ errors.first('CURP') }}</span>
             </vs-col>    
            <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="2">
                <vs-input size="large" v-validate="'required'" label="RFC" placeholder="RFC" name="RFC" v-model="form.rfc" class="mt-5 w-full" />
                <span class="text-danger text-sm" v-show="errors.has('RFC')">{{ errors.first('RFC') }}</span>
            </vs-col>    
            <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="2">
                <vs-input size="large" v-validate="'required'" label="CUIP" placeholder="CUIP" name="CUIP" v-model="form.cuip" class="mt-5 w-full" />
                <span class="text-danger text-sm" v-show="errors.has('CUIP')">{{ errors.first('CUIP') }}</span>
            </vs-col>
            <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="2">
                <vs-input size="large" v-validate="'required'" label="Capacidades" placeholder="Capacidades" name="Capacidades" v-model="form.capacidad" class="mt-5 w-full" />
                <span class="text-danger text-sm" v-show="errors.has('capacidad')">{{ errors.first('capacidad') }}</span>
             </vs-col>

        </vs-row>
        <vs-button type="filled" @click.prevent="submitForm" class="mt-5 block">Guardar</vs-button>
    </form>
    </vx-card>
</template>

<script>
import consultaEmpleadoServicio from '@/services/consultaEmpleado'

export default {


  components: {
    
  },
  data() {
    return {
      form: {
        capacidad: '',
        numeroEmpleado: '',
        nombre: '',
        apellido1: '',
        apellido2: '',
        curp: '',
        rfc: '',
        cuip: '',
        grado: '',
        telefono: '',
        telefono_oficina: '',
        extencion: '',
        telefono_celular: '',
        adscripcion_general: '',
        correo: '',
        descripcion: '',
        escolaridad: '',
        edad: '',
        numeroLicenia: '',
        tipoLicencia: '',
        colonia: '',
        alcaldia: '',
        municipio: '',
        entidadFederativa: '',
        codigoPostal: '',
        state: true,
        created_date:'2021-10-06'

      }
    }
  },
  mounted() {
  },

  methods: {
    submitForm(){
      console.log('enviar');
    },
    consularN(){
      this.mostrarM = false
      this.mostrarM2 = false
      if(isNaN(this.form.numeroEmpleado) || this.form.numeroEmpleado < 1) {
        this.$vs.notify({
                title:'Error',
                text:'Error en la placa escrita',
                color:'danger'})
      }else{
      this.$vs.loading()
        consultaEmpleadoServicio.consultarEmpleado(this.form.numeroEmpleado).then(response => {
          consultaEmpleadoServicio.consultarImagen(this.form.numeroEmpleado).then(response => {
            console.log('response.data.data[0].data', response.data.data[0].data)
          }).catch(error => {
              this.$vs.loading.close()
              console.log(error)
          })
              console.log('response.data.data[0].data', response.data.data[0].data)
              this.form.nombre = response.data.data[0].data.nombre
              this.form.apellido1 = response.data.data[0].data.primer_apellido
              this.form.apellido2 = response.data.data[0].data.segundo_apellido
              if (response.data.data[0].error === 1){
                this.$vs.notify({
                  title:'Error',
                  text:'La placa no existe2',
                  color:'danger'})
              }
                this.$vs.loading.close()
            })
            .catch(error => {
              this.$vs.loading.close()
              console.log(error)
              })
      } 
    },
  },
  watch: {
  },
  computed: {
  }
}
</script>
<style lang="scss">
  .espacio {
  margin-left: 50%;

  }

  .selectTa {
    display:block;
    height:40px;
    width: 200px;
  }
</style>
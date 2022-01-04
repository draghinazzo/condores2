<template>
    <vx-card title="Agregar personalaa" id="parentx-demo-5">
    <form>
        <vs-row vs-align="flex-end"
                vs-type="flex" 
                vs-justify="space-between" vs-w="12">

            <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="2">
                <img v-if="imagen=== '' " class="foto" src="@/assets/images/portrait/small/avatar-s-8.jpg" />
                <img v-else class="foto" :src="`data:image/png;base64, ${imagen}`" />

            </vs-col>  

            <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="2">
                <vs-input v-on:blur="consularN" size="large" v-validate="'required'" label="Numero de empleado" placeholder="Numero de empleado" name="Numero de empleado" v-model="form.numeroEmpleado" class="mt-5 w-full" />
                <span class="text-danger text-sm" v-show="errors.has('numeroEmpleado')">{{ errors.first('numeroEmpleado') }}</span>
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
                <vs-input size="large" v-validate="'required'" label="Grado" placeholder="Grado" name="Grado" v-model="form.grado" class="mt-5 w-full" />
                <span class="text-danger text-sm" v-show="errors.has('grado')">{{ errors.first('grado') }}</span>
             </vs-col>

        </vs-row>

        <vs-row vs-align="flex-end"
                vs-type="flex" 
                vs-justify="space-between" vs-w="12">

             <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="2">
                <vs-input size="large" v-validate="'required'" label="Telefono" placeholder="Telefono" name="Telefono" v-model="form.telefono" class="mt-5 w-full" />
                <span class="text-danger text-sm" v-show="errors.has('telefono')">{{ errors.first('telefono') }}</span>
             </vs-col>    
            <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="2">
                <vs-input size="large" v-validate="'required'" label="Telefono de oficina" placeholder="Telefono de oficina" name="Telefono de oficina" v-model="form.telefono_oficina" class="mt-5 w-full" />
                <span class="text-danger text-sm" v-show="errors.has('telefono_oficina')">{{ errors.first('telefono_oficina') }}</span>
            </vs-col>    
            <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="2">
                <vs-input size="large" v-validate="'required'" label="Extencion" placeholder="Extencion" name="Extencion" v-model="form.extencion" class="mt-5 w-full" />
                <span class="text-danger text-sm" v-show="errors.has('extencion')">{{ errors.first('extencion') }}</span>
            </vs-col>
            <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="2">
                <vs-input size="large" v-validate="'required'" label="Telefono celular" placeholder="Telefono celular" name="Telefono celular" v-model="form.telefono_celular" class="mt-5 w-full" />
                <span class="text-danger text-sm" v-show="errors.has('telefono_celular')">{{ errors.first('telefono_celular') }}</span>
             </vs-col>

        </vs-row>

        <vs-row vs-align="flex-end"
                vs-type="flex" 
                vs-justify="space-between" vs-w="12">

             <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="2">
                <vs-input size="large" v-validate="'required'" label="Adscripcion general" placeholder="Adscripcion general" name="Adscripcion general" v-model="form.adscripcion_general" class="mt-5 w-full" />
                <span class="text-danger text-sm" v-show="errors.has('adscripcion_general')">{{ errors.first('adscripcion_general') }}</span>
             </vs-col>    
            <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="2">
                <vs-input size="large" v-validate="'required'" label="Correo" placeholder="Correo" name="Correo" v-model="form.correo" class="mt-5 w-full" />
                <span class="text-danger text-sm" v-show="errors.has('correo')">{{ errors.first('correo') }}</span>
            </vs-col>    
            <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="2">
                <vs-input size="large" v-validate="'required'" label="Descipcion" placeholder="Descipcion" name="Descipcion" v-model="form.descripcion" class="mt-5 w-full" />
                <span class="text-danger text-sm" v-show="errors.has('descripcion')">{{ errors.first('descripcion') }}</span>
            </vs-col>
            <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="2">
                <vs-input size="large" v-validate="'required'" label="Nivel academico" placeholder="Nivel academico" name="Nivel academico" v-model="form.escolaridad" class="mt-5 w-full" />
                <span class="text-danger text-sm" v-show="errors.has('escolaridad')">{{ errors.first('escolaridad') }}</span>
             </vs-col>

        </vs-row>

        <vs-row vs-align="flex-end"
                vs-type="flex" 
                vs-justify="space-between" vs-w="12">

             <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="2">
                <vs-input size="large" v-validate="'required'" label="Edad" placeholder="Edad" name="Edad" v-model="form.edad" class="mt-5 w-full" />
                <span class="text-danger text-sm" v-show="errors.has('edad')">{{ errors.first('edad') }}</span>
             </vs-col>    
            <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="2">
                <vs-input size="large" v-validate="'required'" label="Antiguedad" placeholder="Antiguedad" name="Antiguedad" v-model="form.antiguedad" class="mt-5 w-full" />
                <span class="text-danger text-sm" v-show="errors.has('antiguedad')">{{ errors.first('antiguedad') }}</span>
            </vs-col>    
            <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="2">
                <vs-input size="large" v-validate="'required'" label="Numero de Licencia" placeholder="Numero de Licencia" name="Numero de Licencia" v-model="form.numeroLicencia" class="mt-5 w-full" />
                <span class="text-danger text-sm" v-show="errors.has('numeroLicencia')">{{ errors.first('numeroLicencia') }}</span>
            </vs-col>
            <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="2">
                Tipo empleado
            <v-select  class="selectTa" v-model="selectTipoE" :options="optionsTipoE" :dir="$vs.rtl ? 'rtl' : 'ltr'"/>
             </vs-col>

        </vs-row>
        <br>
        <vs-row vs-align="flex-end"
                vs-type="flex" 
                vs-justify="space-between" vs-w="12">
            <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="2">
              Sexo
              <v-select  class="selectTa" v-model="selectSexo" :options="optionsSexo" :dir="$vs.rtl ? 'rtl' : 'ltr'" />
            </vs-col>

        </vs-row>
        <vs-button type="filled" @click.prevent="submitForm" class="mt-5 block">Guardar</vs-button>
    </form>
    </vx-card>
</template>

<script>
import consultaEmpleadoServicio from '@/services/consultaEmpleado'
import tipoEServicio from '@/services/misiones/tipoE'
import sexoServicio from '@/services/misiones/sexo'


import vSelect from 'vue-select'
export default {


  components: {
    'v-select': vSelect,
    
  },
  data() {
    return {
      selectSexo: null,
      optionsSexo: [],
      optionsTipoE: [],
      imagen: '',
      selectTipoE: null,
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
        numeroLicencia: '',
        tipoLicencia: '',
        tipo_empleado: '',
        sexo: '',
        colonia: '',
        alcaldia: '',
        municipio: '',
        entidadFederativa: '',
        codigoPostal: '',
        state: true,
        created_date:'2021-10-06'

      },
      queryPage: {
        limit: 10,
        offset: 0,
        nombre: ''
      },
    }
  },
  mounted() {
    this.getTipoE()
    this.getSexo()

  },

  methods: {
    getSexo(){
      sexoServicio.select(this.queryPage)
        .then(response => {
          this.$vs.loading.close()
          this.optionsSexo= response.data.results
        })
        .catch(error => {
          
          this.$vs.loading.close()
          console.log(error)
          })
    },
    getTipoE(){
      tipoEServicio.select(this.queryPage)
        .then(response => {
          console.log(response.data.results)
          this.$vs.loading.close()
          this.optionsTipoE= response.data.results
        })
        .catch(error => {
          
          this.$vs.loading.close()
          console.log(error)
          })
    },
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
        consultaEmpleadoServicio.consultarImagen(this.form.numeroEmpleado).then(response => {

          this.imagen = response.data.data[0].data.imagen
          consultaEmpleadoServicio.consultarEmpleado(this.form.numeroEmpleado).then(response => {
          
              console.log('response.data.data[0].data', response.data.data[0].data)
              this.form.nombre = response.data.data[0].data.nombre
              this.form.apellido1 = response.data.data[0].data.primer_apellido
              this.form.apellido2 = response.data.data[0].data.segundo_apellido
              this.form.curp = response.data.data[0].data.curp
              this.form.rfc = response.data.data[0].data.rfc
              this.form.cuip = response.data.data[0].data.cuip
              this.form.grado = response.data.data[0].data.grado
              this.form.telefono = response.data.data[0].data.telefono
              this.form.telefono_oficina = response.data.data[0].data.telefono_oficina
              this.form.extencion = response.data.data[0].data.extension
              this.form.telefono_celular = response.data.data[0].data.telefono_celular
              this.form.adscripcion_general = response.data.data[0].data.adscripcion_general
              this.form.correo = response.data.data[0].data.correo
              this.form.descripcion = response.data.data[0].data.descripcion
              this.form.escolaridad = response.data.data[0].data.escolaridad
              this.form.edad = response.data.data[0].data.edad
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
        }).catch(error => {
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

  .foto {
    display:block;
    height:150px;
    width: 120px;
  }
</style>
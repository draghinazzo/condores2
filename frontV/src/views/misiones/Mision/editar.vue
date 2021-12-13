<template>
    <vx-card title="Editar Mision" id="parentx-demo-5">
        <form>
        <vs-row>
          <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="1" vs-sm="4" vs-xs="12" >
            
            <vs-input size="large" v-validate="'required'" label="# de Empleado" v-on:blur="consularN" placeholder="Numero de Empleado" name="Numero de Empleado" v-model="form.numeroEmpleado" class="mt-5 w-full" />
            <span class="text-danger text-sm" v-show="errors.has('numeroEmpleado')">{{ errors.first('Numero de Empleado') }}</span>

          </vs-col>
          
          <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="2" vs-sm="4" vs-xs="12" >

            <vs-input size="large" v-validate="'required'" label="Nombre" placeholder="Nombre" name="Nombre" v-model="form.nombre" class="mt-5 w-full " :disabled='true'/>
            <span class="text-danger text-sm" v-show="errors.has('Nombre')">{{ errors.first('Nombre') }}</span>

          </vs-col>
          
          <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="2" vs-sm="4" vs-xs="12" >
            
            <vs-input size="large" v-validate="'required'" label="Apellido1" placeholder="Apellido1" name="Apellido1" v-model="form.apellido1" class="mt-5 w-full " :disabled='true'/>
            <span class="text-danger text-sm" v-show="errors.has('Apellido1')">{{ errors.first('Apellido1') }}</span>

          </vs-col>
          
          <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="2" vs-sm="4" vs-xs="12" >

            <vs-input size="large" v-validate="'required'" label="Apellido2" placeholder="Apellido2" name="Apellido2" v-model="form.apellido2" class="mt-5 w-full " :disabled='true'/>
            <span class="text-danger text-sm" v-show="errors.has('Apellido2')">{{ errors.first('Apellido2') }}</span>
            
          </vs-col>
          
          <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="2" vs-sm="4" vs-xs="12" >
            <vs-input size="large" v-validate="'required'" label="cuip" placeholder="cuip" name="cuip" v-model="form.cuip" class="mt-5 w-full " :disabled='true'/>
            <span class="text-danger text-sm" v-show="errors.has('cuip')">{{ errors.first('cuip') }}</span>
          </vs-col>
          
          <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="3" vs-sm="4" vs-xs="12" >
            Tipo empleado
            <v-select  class="selectTa" v-model="selectTipoE" :options="optionsTipoE" :dir="$vs.rtl ? 'rtl' : 'ltr'" :disabled='true' />
          </vs-col>
        </vs-row>

        <vs-row>
          <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="2" vs-sm="4" vs-xs="12" >
            <vs-input size="large" v-validate="'required'" label="curp" placeholder="curp" name="curp" v-model="form.curp" class="mt-5 w-full " :disabled='true'/>
            <span class="text-danger text-sm" v-show="errors.has('curp')">{{ errors.first('curp') }}</span>
          </vs-col>
          <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="2" vs-sm="4" vs-xs="12" >
          <vs-input size="large" v-validate="'required'" label="rfc" placeholder="rfc" name="rfc" v-model="form.rfc" class="mt-5 w-full " :disabled='true'/>
            <span class="text-danger text-sm" v-show="errors.has('rfc')">{{ errors.first('rfc') }}</span>
          </vs-col>
          <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="3" vs-sm="4" vs-xs="12" >
            <label> Fecha Nacimiento </label>
            <flat-pickr placeholder="Fecha de inicio" v-model="form.fechaNacimiento" :config="configdateTimePicker" :disabled='true'/>
          </vs-col>
          <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="3" vs-sm="4" vs-xs="12" >
            <label> Fecha Alta </label>
            <flat-pickr placeholder="Fecha de inicio" v-model="form.fechaAlta" :config="configdateTimePicker" :disabled='true'/>
          </vs-col>
          <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="2" vs-sm="4" vs-xs="12" >
            Sexo
            <v-select  class="selectTa" v-model="selectSexo" :options="optionsSexo" :dir="$vs.rtl ? 'rtl' : 'ltr'" :disabled='true' />
          </vs-col>
        </vs-row>

        <br><br>
        <vs-row>
          <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="3" vs-sm="4" vs-xs="12" >
            Direccion
            <v-select  class="selectTa" v-model="selecDireccion" :options="optionsDireccion" :dir="$vs.rtl ? 'rtl' : 'ltr'" />
          </vs-col>
        </vs-row>

        <br><br>
        <vs-row>
          <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="3" vs-sm="4" vs-xs="12" >
            Helicoptero
            <v-select  class="selectTa" v-model="selechelicoptero" :options="optionsHelicoptero" :dir="$vs.rtl ? 'rtl' : 'ltr'" />
          </vs-col>
        </vs-row>

        <br><br>
        <vs-row>
          <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="3" vs-sm="4" vs-xs="12" >
            Medio
            <v-select  class="selectTa" v-model="selectMedio" :options="optionsMedio" :dir="$vs.rtl ? 'rtl' : 'ltr'" />
          </vs-col>
        </vs-row>

        <br><br>
        <vs-row>
          <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="3" vs-sm="4" vs-xs="12" >
            Servicio
            <v-select  class="selectTa" v-model="selectServicio" :options="optionsServicio" :dir="$vs.rtl ? 'rtl' : 'ltr'" />
          </vs-col>
        </vs-row>

        <br><br>
        <vs-row>
          <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="3" vs-sm="4" vs-xs="12" >
            Solicitante
            <v-select  class="selectTa" v-model="selectSolicitante" :options="optionsSolicitante" :dir="$vs.rtl ? 'rtl' : 'ltr'" />
          </vs-col>
        </vs-row>

        <br><br>
        <vs-row>
          
        </vs-row>

        <br><br>
        <vs-row>
          
        </vs-row>
        

        <vs-button type="filled" @click.prevent="submitForm" class="mt-5 block">Guardar</vs-button>

      </form>
    </vx-card>
</template>
<script>
import servicio from '@/services/misiones/mision'
import consultaEmpleadoServicio from '@/services/consultaEmpleado'
import Datepicker from 'vuejs-datepicker';
import flatPickr from 'vue-flatpickr-component';
import 'flatpickr/dist/flatpickr.css';
import {Spanish as espa} from 'flatpickr/dist/l10n/es.js';
import vSelect from 'vue-select'
import helicopteroServicio from '@/services/misiones/helicoptero'
import direccionMServicio from '@/services/misiones/direccionM'
import medioServicio from '@/services/misiones/medio'
import servicioServicio from '@/services/misiones/servicio'
import solicitanteServicio from '@/services/misiones/solicitante'
import sexoServicio from '@/services/misiones/sexo'
import tipoEServicio from '@/services/misiones/tipoE'

export default {
  components: {
    Datepicker,
    flatPickr,
    'v-select': vSelect,
  },
  data() {
    return {
      selectTipoE: {id:''},
      selectSexo: null,
      selectSolicitante: null,
      selectServicio: null,
      selectMedio: null,
      selecDireccion: null,
      selechelicoptero: null,
      queryPage: {
        limit: 10,
        offset: 0,
        nombre: ''
      },
      optionsTipoE: [],
      optionsSexo: [],
      optionsSolicitante: [],
      optionsServicio: [],
      optionsDireccion: [],
      optionsHelicoptero: [],
      optionsMedio: [],
      mostrarM2: false,
      mostrarM: false,
      configdateTimePicker: {
        locale: espa
      },
      id: null,
      form: {
        nombre: '',
        apellido1: '',
        apellido2: '',
        numeroEmpleado: '',
        cuip: '',
        curp: '',
        rfc: '',
        fechaAlta: '',
        fechaNacimiento: '',
        state: true,
        created_date:'2021-10-06',
        tipoEmpleado: '',
        sexo: '',
        solicitante: '',
        servicio: '',
        ubicacion: '',
        helicoptero: '',
        medio: ''


      }
    }
  },
  mounted() {
    this.id = this.$route.params.id
    this.getHelicopteros()
    this.getDireccionM()
    this.getMedio()
    this.getDatos()
    this.getServicio()
    this.getSolicitante()
    this.getSexo()
    this.getTipoE()
  },

  methods: {
    
    getTipoE(){
      tipoEServicio.select(this.queryPage)
        .then(response => {
          this.$vs.loading.close()
          this.optionsTipoE= response.data.results
        })
        .catch(error => {
          
          this.$vs.loading.close()
          console.log(error)
          })
    },
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
    getSolicitante(){
      solicitanteServicio.select(this.queryPage)
        .then(response => {
          this.$vs.loading.close()
          this.optionsSolicitante= response.data.results
        })
        .catch(error => {
          
          this.$vs.loading.close()
          console.log(error)
          })
    },
    getServicio(){
      servicioServicio.select(this.queryPage)
        .then(response => {
          this.$vs.loading.close()
          this.optionsServicio= response.data.results
        })
        .catch(error => {
          
          this.$vs.loading.close()
          console.log(error)
          })
    },
    getMedio(){
      medioServicio.select(this.queryPage)
        .then(response => {
          this.$vs.loading.close()
          this.optionsMedio= response.data.results
        })
        .catch(error => {
          
          this.$vs.loading.close()
          console.log(error)
          })
    },
    getDireccionM(){
      direccionMServicio.select(this.queryPage)
        .then(response => {
          this.$vs.loading.close()
          this.optionsDireccion = response.data.results
        })
        .catch(error => {
          
          this.$vs.loading.close()
          console.log(error)
          })
    },
    getHelicopteros(){
      helicopteroServicio.select(this.queryPage)
        .then(response => {
          this.$vs.loading.close()
          this.optionsHelicoptero = response.data.results
        })
        .catch(error => {
          
          this.$vs.loading.close()
          console.log(error)
          })
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
              console.log(response.data.data[0].data)
              this.form.nombre = response.data.data[0].data.nombre
              this.form.apellido1 = response.data.data[0].data.primer_apellido
              this.form.apellido2 = response.data.data[0].data.segundo_apellido
              this.form.fechaNacimiento = response.data.data[0].data.fecha_nacimiento
              this.form.fechaAlta = response.data.data[0].data.fecha_alta
              this.form.rfc = response.data.data[0].data.rfc
              this.form.curp = response.data.data[0].data.curp
              this.form.cuip = response.data.data[0].data.cuip
              var label
              (response.data.data[0].data.sexoId === 1) ? label = 'Masculino': label = 'Femenino'
              this.selectSexo = {id: response.data.data[0].data.sexoId, label: label}

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
    getDatos(){
      servicio.obtenerId(this.id).then(response => {
            console.log('responseMantenimiento', response.data)
            this.selechelicoptero = {id: response.data.helicopteroId, label: response.data.helicoptero}
            this.selecDireccion = {id: response.data.ubicacionID, label: response.data.ubicacion}
            this.selectMedio = {id: response.data.medioId, label: response.data.medio}
            this.selectServicio = {id: response.data.servicioId, label: response.data.servicio}
            this.selectSolicitante = {id: response.data.solicitanteId, label: response.data.solicitante}
            this.selectSexo = {id: response.data.sexoId, label: response.data.sexo}
            this.selectTipoE = {id: response.data.tipoEmpleadoId, label: response.data.tipoEmpleado}

            this.form.fechaNacimiento = response.data.fechaNacimiento
            this.form.fechaAlta = response.data.fechaAlta
            this.form.rfc = response.data.rfc
            this.form.curp = response.data.curp
            this.form.cuip = response.data.cuip
            this.form.apellido1 = response.data.apellido1
            this.form.apellido2 = response.data.apellido2
            this.form.numeroEmpleado = response.data.numeroEmpleado
            this.form.nombre = response.data.nombre
            this.$vs.loading.close()
          })
          .catch(error => console.log(error))
    },
    formatoFecha(fecha, formato) {
      const map = {
          dd: ("0" + fecha.getDate()).slice(-2),
          mm:("0" + (fecha.getMonth() + 1)).slice(-2),
          yy: fecha.getFullYear()
      }
      return formato.replace(/dd|mm|yy|yyy/gi, matched => map[matched])
    },
    submitForm() {
      this.form.helicoptero = this.selechelicoptero.id
      this.form.ubicacion = this.selecDireccion.id
      this.form.medio = this.selectMedio.id
      this.form.servicio = this.selectServicio.id
      this.form.solicitante = this.selectSolicitante.id
      this.form.sexo = this.selectSexo.id
      this.form.tipoEmpleado = this.selectTipoE.id
      this.$validator.validateAll().then(result => {
        this.$vs.loading()
        const hoy = new Date();
        this.form.created_date = this.formatoFecha(hoy, 'yy-mm-dd')
        if(result) {
          // if form have no errors
          servicio.actualizarId(this.id, this.form).then(response => {
            console.log('response', response)
            this.$emit('cerrar', false)
            this.$vs.loading.close()
          })
          .catch(error => console.log(error))
        }else{
          // form have errors
          this.$vs.loading.close()
         }
      })
    }
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
    width:200px;
  }
</style>
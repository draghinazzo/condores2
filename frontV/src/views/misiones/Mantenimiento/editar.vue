<template>
    <vs-popup class="holamundo" title="Editar" :active.sync="verL">
      <form>
        <flat-pickr placeholder="Fecha de inicio" v-model="form.fechaInicio" :config="configdateTimePicker"/>
        <label v-if="mostrarM2" class="mensajeE"> Campo necesario</label>
        <br>
        <br>
        Helicoptero
        <v-select  stylr="wi"  v-model="selechelicoptero" :options="options" :dir="$vs.rtl ? 'rtl' : 'ltr'" /><br>
         <label v-if="mostrarM" class="mensajeE"> Campo necesario</label>

        <vs-input type="number" size="large" v-validate="'required'" label="Placa" placeholder="Placa" name="Placa" v-on:blur="consularN" v-model="form.numeroEmpleado" class="mt-5 w-full" />
        <span class="text-danger text-sm" v-show="errors.has('Placa')">{{ errors.first('Placa') }}</span>

        <vs-input size="large" v-validate="'required'" label="Nombre" placeholder="Nombre" name="Nombre" v-model="form.nombre" class="mt-5 w-full" />
        <span class="text-danger text-sm" v-show="errors.has('Nombre')">{{ errors.first('Nombre') }}</span>

        <vs-input size="large" v-validate="'required'" label="Apellido 1" placeholder="Apellido 1" name="Apellido 1" v-model="form.apellido1" class="mt-5 w-full" />
        <span class="text-danger text-sm" v-show="errors.has('Apellido 1')">{{ errors.first('Apellido 1') }}</span>

        <vs-input size="large" v-validate="'required'" label="Apellido 2" placeholder="Apellido 2" name="Apellido 2" v-model="form.apellido2" class="mt-5 w-full" />
        <span class="text-danger text-sm" v-show="errors.has('Apellido 2')">{{ errors.first('Apellido 2') }}</span>

        <vs-button type="filled" @click.prevent="submitForm" class="mt-5 block">Guardar</vs-button>
      </form>
    </vs-popup>
</template>
<script>
import helicopteroServicio from '@/services/misiones/helicoptero'
import servicio from '@/services/misiones/mantenimiento'
import consultaEmpleadoServicio from '@/services/consultaEmpleado'
import Datepicker from 'vuejs-datepicker';
import flatPickr from 'vue-flatpickr-component';
import 'flatpickr/dist/flatpickr.css';
import {Spanish as espa} from 'flatpickr/dist/l10n/es.js';
import vSelect from 'vue-select'

export default {
  components: {
    Datepicker,
    flatPickr,
    'v-select': vSelect,
  },
  data() {
    return {
      mostrarM2: false,
      mostrarM: false,
      selechelicoptero: null,
      options: [],
      queryPage: {
        limit: 10,
        offset: 0,
        nombre: ''
      },
      configdateTimePicker: {
        locale: espa
      },
      form: {
        helicoptero: null,
        fechaInicio: null,
        apellido1: null,
        apellido2: null,
        numeroEmpleado: null,
        nombre: '',
        state: true,
        created_date: null

      }
    }
  },
  mounted() {
    this.getHelicopteros()
  },
  props: {
    ver: {
      type: Boolean,
      required: true
    },
    id: {
      type: Number,
      required: true
    }
  },

  methods: {
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
    getHelicopteros(){
      helicopteroServicio.select(this.queryPage)
        .then(response => {
          this.$vs.loading.close()
          this.options = response.data.results
          console.log('this.options', this.options)
        })
        .catch(error => {
          
          this.$vs.loading.close()
          console.log(error)
          })
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
    id(){
      this.$vs.loading()
      servicio.obtenerId(this.id).then(response => {
            console.log('responseMantenimiento', response.data)
            this.selechelicoptero = {id: response.data.helicopteroId, label: response.data.placaH}
            console.log('this.form.selechelicoptero', this.form.selechelicoptero)

            this.form.fechaInicio = response.data.fechaInicio
            this.form.apellido1 = response.data.apellido1
            this.form.apellido2 = response.data.apellido2
            this.form.numeroEmpleado = response.data.numeroEmpleado
            this.form.nombre = response.data.nombre
            this.$vs.loading.close()
          })
          .catch(error => console.log(error))
    },
  },
  computed: {
    verL: {
      get () {
        return this.ver
      },
      set (value) {
        this.$emit('cerrar', value)
      }
    }
  }
}
</script>
<style type="text/css">
  .mensajeE {
    background-color: white;
    color: red;
    position: relative;
    bottom: 20px;
  }
</style>
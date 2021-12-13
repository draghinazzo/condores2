<template>
    <vs-popup class="holamundo" title="Formulario" :active.sync="verL">
      <form>
      <vs-row>
        <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="6">
          <flat-pickr placeholder="Fecha de inicio" v-model="form.fechaInicio" :config="configdateTimePicker"/>
          <label v-if="mostrarFI" class="mensajeE"> Campo necesario</label>
        </vs-col>
        <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="6">
          <flat-pickr placeholder="Fecha de fin" v-model="form.fechaFin" :config="configdateTimePicker"/>
          <label v-if="mostrarFF" class="mensajeE"> Campo necesario</label>
        </vs-col>
      </vs-row>
        
        <vs-input size="large" v-validate="'required'" label="Nombre del curso" placeholder="Nombre del curso" name="Nombre del curso" v-model="form.nombreCurso" class="mt-5 w-full" />
        <span class="text-danger text-sm" v-show="errors.has('nombreCurso')">{{ errors.first('nombreCurso') }}</span>

        Instructor
        <v-select  stylr="wi" v-model="selecInstructor" :options="options" :dir="$vs.rtl ? 'rtl' : 'ltr'" /><br>
         <label v-if="mostrarM" class="mensajeE"> Campo necesario</label>

        <vs-button type="filled" @click.prevent="submitForm" class="mt-5 block">Guardar</vs-button>
      </form>
    </vs-popup>
</template>
<script>
import servicio from '@/services/capacitacion/instructor'
import servicioCurso from '@/services/capacitacion/curso'

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
      mostrarM: false,
      selecInstructor: null,
      options: [],
      mostrarFI: false,
      mostrarFF: false,
      queryPage: {
        limit: 10,
        offset: 0,
        nombre: ''
      },
      form: {
        nombreCurso: '',
        fechaInicio: null,
        fechaFin: null,
        instructor: '',
        state: true,
        created_date:'2021-10-06'

      },
      configdateTimePicker: {
        locale: espa
      },
    }
  },
  mounted() {
    this.getInstructor()
  },
  props: {
    ver: {
      type: Boolean,
      required: true
    }
  },

  methods: {
    getInstructor(){
      servicio.select(this.queryPage)
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
    borrar(){ 
        this.form.nombreCurso = null
        this.form.fechaInicio= null
        this.form.selecInstructor= null
        this.form.fechaFin= null
        this.form.state= null
    },
    submitForm() {
        const hoy = new Date();
        this.form.created_date = this.formatoFecha(hoy, 'yy-mm-dd')
        let val = 0
        this.$validator.validateAll().then(result => {
        
        const hoy = new Date();
        this.form.created_date = this.formatoFecha(hoy, 'yy-mm-dd')
        console.log('fecahII', this.form.fechaInicio);
        if (this.form.fechaInicio == null ) {
              this.mostrarFI = true
              val = 1
             } else { this.mostrarFI = false }
        if (this.form.fechaFin == null ) {
               this.mostrarFF = true
              val = 1
             } else { this.mostrarFF = false }
        if (this.form.selecInstructor == null ) {
               this.mostrarM = true
              val = 1
             } else { this.mostrarFM = false }
        
        if(val === 1) {
          if(result) {
              
              
              

            this.$vs.loading()
            // if form have no errors
            this.form.instructor = this.selecInstructor.id
            servicioCurso.crear(this.form).then(response => {
              console.log('response', response)
              this.borrar()
              this.$emit('cerrar', false)
              this.$vs.loading.close()
            })
            .catch(error => 
            { this.$vs.loading.close()
              console.log(error)
              })
          }else{
            // form have errors
            this.$vs.loading.close()
          }
        }
      })
    }
  },
  watch: {
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
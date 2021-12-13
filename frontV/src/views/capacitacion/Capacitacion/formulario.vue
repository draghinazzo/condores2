<template>
    <vs-popup class="holamundo" title="Formulario" :active.sync="verL">
      <form>
        
        <vs-input size="large" v-validate="'required'" label="Numero de empleado" placeholder="Numero de empleado" name="Numero de empleado" v-model="form.numeroEmpleado" class="mt-5 w-full" />
        <span class="text-danger text-sm" v-show="errors.has('numeroEmpleado')">{{ errors.first('numeroEmpleado') }}</span>

        Curso
        <v-select  stylr="wi" v-model="selecInstructor" :options="options" :dir="$vs.rtl ? 'rtl' : 'ltr'" /><br>
         <label v-if="mostrarM" class="mensajeE"> Campo necesario</label>

        <vs-button type="filled" @click.prevent="submitForm" class="mt-5 block">Guardar</vs-button>
      </form>
    </vs-popup>
</template>
<script>
import servicio from '@/services/capacitacion/capacitacion'

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
        numeroEmpleado: '',
        curso: '',
        state: true,
        created_date:'2021-10-06'

      },
      configdateTimePicker: {
        locale: espa
      },
    }
  },
  mounted() {
    this.getCurso()
  },
  props: {
    ver: {
      type: Boolean,
      required: true
    }
  },

  methods: {
    getCurso(){
      servicio.select(this.queryPage)
        .then(response => {
          this.$vs.loading.close()
          this.options = response.data.results
          console.log('this.curso', this.options)
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
        this.form.numeroEmpleado = null
    },
    submitForm() {
        const hoy = new Date();
        this.form.created_date = this.formatoFecha(hoy, 'yy-mm-dd')
        let val = 0
        this.$validator.validateAll().then(result => {
        
        const hoy = new Date();
        this.form.created_date = this.formatoFecha(hoy, 'yy-mm-dd')
        console.log('fecahII', this.form.fechaInicio);
      
        if (this.form.selecInstructor == null ) {
               this.mostrarM = true
              val = 1
             } else { this.mostrarM = false }
        
        if(val === 1) {
          if(result) {
              
              
              

            this.$vs.loading()
            // if form have no errors
            this.form.instructor = this.selecInstructor.id
            servicio.crear(this.form).then(response => {
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
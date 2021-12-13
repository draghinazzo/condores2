<template>
    <vs-popup class="holamundo" title="Formulario" :active.sync="verL">
      <form>

        <vs-input size="large" v-validate="'required'" label="Placa" placeholder="Placa" name="Placa" v-model="form.placa" class="mt-5 w-full" />
        <span class="text-danger text-sm" v-show="errors.has('Placa')">{{ errors.first('Placa') }}</span>

        <vs-input size="large" v-validate="'required'" label="Modelo" placeholder="Modelo" name="Modelo" v-model="form.modelo" class="mt-5 w-full" />
        <span class="text-danger text-sm" v-show="errors.has('Modelo')">{{ errors.first('Modelo') }}</span>

        <vs-input size="large" v-validate="'required'" label="Año" placeholder="Año" name="Año" v-model="form.year" class="mt-5 w-full" />
        <span class="text-danger text-sm" v-show="errors.has('Año')">{{ errors.first('Año') }}</span>

        <vs-input size="large" v-validate="'required'" label="Marca" placeholder="Marca" name="Marca" v-model="form.marca" class="mt-5 w-full" />
        <span class="text-danger text-sm" v-show="errors.has('Marca')">{{ errors.first('Marca') }}</span>

        <vs-input size="large" v-validate="'required'" label="Estatus" placeholder="Estatus" name="Estatus" v-model="form.status" class="mt-5 w-full" />
        <span class="text-danger text-sm" v-show="errors.has('Estatus')">{{ errors.first('Estatus') }}</span>

        <vs-button type="filled" @click.prevent="submitForm" class="mt-5 block">Guardar</vs-button>
      </form>
    </vs-popup>
</template>
<script>
import servicio from '@/services/misiones/helicoptero'
import Datepicker from 'vuejs-datepicker';
import flatPickr from 'vue-flatpickr-component';
import 'flatpickr/dist/flatpickr.css';
import {Spanish as espa} from 'flatpickr/dist/l10n/es.js';
import vSelect from 'vue-select'
import { Validator } from 'vee-validate';

const dict = {
  custom: {
    Placa: {
      required: 'La placa es necesaria'
    },
    Modelo: {
      required: 'El modelo es necesario'
    },
    Año: {
      required: 'El año es necesario'
    },
    Marca: {
      required: 'La marca es necesaria'
    },
    Estatus: {
      required: 'El estatus es necesario'
    },
  }
};
Validator.localize('en', dict);
export default {
  components: {
    Datepicker,
    flatPickr,
    'v-select': vSelect,
  },
  data() {
    return {
      selechelicoptero:null,
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
        placa: null,
        modelo: '',
        year: null,
        marca: null,
        status: null,
        state: true,
        created_date:'2021-10-06'

      }
    }
  },
  mounted() {
    
  },
  props: {
    ver: {
      type: Boolean,
      required: true
    }
  },

  methods: {
    buscar(){
      console.log('this.form.helicoptero', this.form.helicoptero)
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
      console.log('formmmm', this.form)
      this.$validator.validateAll().then(result => {
        const hoy = new Date();
        this.form.created_date = this.formatoFecha(hoy, 'yy-mm-dd')
        if(result) {
          this.$vs.loading()
          // if form have no errors
          servicio.crear(this.form).then(response => {
            console.log('response', response)
            this.$emit('cerrar', false)
            this.$vs.loading.close()
          })
          .catch(error => {
            this.$vs.loading.close()
            console.log(error)
            })
        }else{
          console.log('Errorrrr llenado');
          // form have errors
          this.$vs.loading.close()
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
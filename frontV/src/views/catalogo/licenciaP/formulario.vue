<template>
    <vs-popup class="Institucion" title="Formulario" :active.sync="verL">
      <form>
        <vs-input size="large" v-validate="'required'" label="Numero de licencia" placeholder="Numero de licencia" name="numeroLicencia" v-model="form.numeroLicencia" class="mt-5 w-full" />
        <span class="text-danger text-sm" v-show="errors.has('numeroLicencia')">{{ errors.first('numeroLicencia') }}</span>

        <vs-input size="large" v-validate="'required'" label="Tipo de licencia" placeholder="Tipo de licencia" name="tipoLicencia" v-model="form.tipoLicencia" class="mt-5 w-full" />
        <span class="text-danger text-sm" v-show="errors.has('tipoLicencia')">{{ errors.first('tipoLicencia') }}</span>

        <br>
        <flat-pickr placeholder="Vigencia" v-model="form.vigencia" :config="configdateTimePicker"/>
          

        <vs-button type="filled" @click.prevent="submitForm" class="mt-5 block">Guardar</vs-button>
      </form>
    </vs-popup>
</template>
<script>
import servicio from '@/services/catalogos/licenciaP'
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
      configdateTimePicker: {
        locale: espa
      },
      form: {
        numeroLicencia: '',
        vigencia: '',
        tipoLicencia: '',
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
          servicio.crear(this.form).then(response => {
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
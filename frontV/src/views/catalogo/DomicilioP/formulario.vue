<template>
    <vs-popup class="Institucion" title="Formulario" :active.sync="verL">
      <form>
        <vs-input size="large" v-validate="'required'" label="Colonia" placeholder="Colonia" name="Colonia" v-model="form.colonia" class="mt-5 w-full" />
        <span class="text-danger text-sm" v-show="errors.has('Colonia')">{{ errors.first('Colonia') }}</span>

        <vs-input size="large" v-validate="'required'" label="Alcaldia" placeholder="Alcaldia" name="Alcaldia" v-model="form.alcaldia" class="mt-5 w-full" />
        <span class="text-danger text-sm" v-show="errors.has('Alcaldia')">{{ errors.first('Alcaldia') }}</span>

        <vs-input size="large" v-validate="'required'" label="Municipio" placeholder="Municipio" name="Municipio" v-model="form.municipio" class="mt-5 w-full" />
        <span class="text-danger text-sm" v-show="errors.has('Municipio')">{{ errors.first('Municipio') }}</span>

        <vs-input size="large" v-validate="'required'" label="Entidad Federativa" placeholder="Entidad Federativa" name="Entidad Federativa" v-model="form.entidadFederativa" class="mt-5 w-full" />
        <span class="text-danger text-sm" v-show="errors.has('entidadFederativa')">{{ errors.first('entidadFederativa') }}</span>

        <vs-input size="large" v-validate="'required'" label="Codigo Postal" placeholder="Codigo Postal" name="Codigo Postal" v-model="form.codigoPostal" class="mt-5 w-full" />
        <span class="text-danger text-sm" v-show="errors.has('codigoPostal')">{{ errors.first('codigoPostal') }}</span>

        <vs-button type="filled" @click.prevent="submitForm" class="mt-5 block">Guardar</vs-button>
      </form>
    </vs-popup>
</template>
<script>
import servicio from '@/services/catalogos/domicilioP'

export default {
  components: {
  },
  data() {
    return {
      form: {
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
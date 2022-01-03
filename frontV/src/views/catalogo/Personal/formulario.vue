<template>
    <vs-popup class="Institucion" title="Formulario" :active.sync="verL">
      <form>
        <vs-input size="large" v-validate="'required'" label="Nombre" placeholder="Nombre" name="Nombre" v-model="form.nombre" class="mt-5 w-full" />
        <span class="text-danger text-sm" v-show="errors.has('Nombre')">{{ errors.first('Nombre') }}</span>

        <vs-input size="large" v-validate="'required'" label="Apellido1" placeholder="Apellido1" name="Apellido1" v-model="form.apellido1" class="mt-5 w-full" />
        <span class="text-danger text-sm" v-show="errors.has('Apellido1')">{{ errors.first('Apellido1') }}</span>

        <vs-input size="large" v-validate="'required'" label="Apellido2" placeholder="Apellido2" name="Apellido2" v-model="form.apellido2" class="mt-5 w-full" />
        <span class="text-danger text-sm" v-show="errors.has('Apellido2')">{{ errors.first('Apellido2') }}</span>

        <vs-input size="large" v-validate="'required'" label="CURP" placeholder="CURP" name="CURP" v-model="form.curp" class="mt-5 w-full" />
        <span class="text-danger text-sm" v-show="errors.has('CURP')">{{ errors.first('CURP') }}</span>

        <vs-input size="large" v-validate="'required'" label="RFC" placeholder="RFC" name="RFC" v-model="form.rfc" class="mt-5 w-full" />
        <span class="text-danger text-sm" v-show="errors.has('RFC')">{{ errors.first('RFC') }}</span>

        <vs-input size="large" v-validate="'required'" label="CUIP" placeholder="CUIP" name="CUIP" v-model="form.cuip" class="mt-5 w-full" />
        <span class="text-danger text-sm" v-show="errors.has('CUIP')">{{ errors.first('CUIP') }}</span>

        <vs-button type="filled" @click.prevent="submitForm" class="mt-5 block">Guardar</vs-button>
      </form>
    </vs-popup>
</template>
<script>
import servicio from '@/services/catalogos/persona'

export default {
  components: {
  },
  data() {
    return {
      form: {
        nombre: '',
        apellido1: '',
        apellido2: '',
        curp: '',
        rfc: '',
        cuip: '',
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
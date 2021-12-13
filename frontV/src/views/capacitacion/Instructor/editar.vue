<template>
    <vs-popup class="holamundo" title="Formulario" :active.sync="verL">
      <form>
        <vs-input size="large" v-validate="'required'" label="Nombre" placeholder="Nombre" name="Nombre" v-model="form.nombre" class="mt-5 w-full" />
        <span class="text-danger text-sm" v-show="errors.has('Nombre')">{{ errors.first('Nombre') }}</span>

        <vs-input size="large" v-validate="'required'" label="Apellido 1" placeholder="Apellido 1" name="Apellido 1" v-model="form.apellido1" class="mt-5 w-full" />
        <span class="text-danger text-sm" v-show="errors.has('Apellido1')">{{ errors.first('Apellido1') }}</span>

        <vs-input size="large" v-validate="'required'" label="apellido 2" placeholder="apellido 2" name="apellido 2" v-model="form.apellido2" class="mt-5 w-full" />
        <span class="text-danger text-sm" v-show="errors.has('apellido2')">{{ errors.first('apellido2') }}</span>

        <vs-input size="large" v-validate="'required'" label="especialidad" placeholder="especialidad" name="especialidad" v-model="form.especialidad" class="mt-5 w-full" />
        <span class="text-danger text-sm" v-show="errors.has('especialidad')">{{ errors.first('especialidad') }}</span>

        <vs-button type="filled" @click.prevent="submitForm" class="mt-5 block">Guardar</vs-button>
      </form>
    </vs-popup>
</template>
<script>
import servicio from '@/services/capacitacion/instructor'

export default {
  components: {
  },
  data() {
    return {
      form: {
        nombre: '',
        apellido1: '',
        apellido2: '',
        especialidad: '',
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
    },
    id: {
      type: Number,
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
            console.log('response', response.data.nombre)
            this.form.nombre = response.data.nombre
            this.form.apellido1 = response.data.apellido1
            this.form.apellido2 = response.data.nombre
            this.form.especialidad = response.data.especialidad
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
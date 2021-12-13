<template>
    <vs-popup class="holamundo" title="Editar" :active.sync="verL">
      <form>
        <vs-input size="large" v-validate="'required'" label="Medio" placeholder="Medio" name="Medio" v-model="form.nombre" class="mt-5 w-full" />
        <span class="text-danger text-sm" v-show="errors.has('Medio')">{{ errors.first('Medio') }}</span>

        <vs-button type="filled" @click.prevent="submitForm" class="mt-5 block">Guardar</vs-button>
      </form>
    </vs-popup>
</template>
<script>
import servicio from '@/services/catalogos/servicio'

export default {
  components: {
  },
  data() {
    return {
      form: {
        nombre: '',
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
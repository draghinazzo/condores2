<template>
    <vs-popup class="holamundo" title="Editar" :active.sync="verL">
      <form>
        <vs-input size="large" v-validate="'required'" label="Placa" placeholder="Placa" name="Placa" v-model="form.placa" class="mt-5 w-full" />
        <span class="text-danger text-sm" v-show="errors.has('Placa')">{{ errors.first('Placa') }}</span>

        <vs-input size="large" v-validate="'required'" label="Modelo" placeholder="Modelo" name="Modelo" v-model="form.modelo" class="mt-5 w-full" />
        <span class="text-danger text-sm" v-show="errors.has('modelo')">{{ errors.first('modelo') }}</span>

        <vs-input size="large" v-validate="'required'" label="Año" placeholder="Año" name="Año" v-model="form.year" class="mt-5 w-full" />
        <span class="text-danger text-sm" v-show="errors.has('year')">{{ errors.first('year') }}</span>

        <vs-input size="large" v-validate="'required'" label="Marca" placeholder="Marca" name="Marca" v-model="form.marca" class="mt-5 w-full" />
        <span class="text-danger text-sm" v-show="errors.has('marca')">{{ errors.first('marca') }}</span>

        <vs-input size="large" v-validate="'required'" label="Estatus" placeholder="Estatus" name="Estatus" v-model="form.status" class="mt-5 w-full" />
        <span class="text-danger text-sm" v-show="errors.has('status')">{{ errors.first('status') }}</span>

        <vs-button type="filled" @click.prevent="submitForm" class="mt-5 block">Guardar</vs-button>
      </form>
    </vs-popup>
</template>
<script>
import servicio from '@/services/misiones/helicoptero'

export default {
  components: {
  },
  data() {
    return {
      form: {
        placa: '',
        modelo: '',
        year: '',
        marca: '',
        status: '',
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
            console.log('responseHelicoptero', response.data)
            this.form.placa = response.data.placa
            this.form.modelo = response.data.modelo
            this.form.year = response.data.year
            this.form.marca = response.data.marca
            this.form.status = response.data.status
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
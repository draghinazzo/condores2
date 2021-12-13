<template>
    <vs-popup class="holamundo" title="Formulario" :active.sync="verL">
      <form>
        
        <vs-input size="large" v-validate="'required'" label="Calle" placeholder="Calle" name="Calle" v-model="form.calle" class="mt-5 w-full" />
        <span class="text-danger text-sm" v-show="errors.has('Calle')">{{ errors.first('Calle') }}</span>

        <vs-input size="large" v-validate="'required'" label="Colonia" placeholder="Colonia" name="Colonia" v-model="form.colonia" class="mt-5 w-full" />
        <span class="text-danger text-sm" v-show="errors.has('Colonia')">{{ errors.first('Colonia') }}</span>

        <vs-input size="large" v-validate="'required'" label="Alcaldia" placeholder="Alcaldia" name="Alcaldia" v-model="form.alcaldia" class="mt-5 w-full" />
        <span class="text-danger text-sm" v-show="errors.has('Alcaldia')">{{ errors.first('Alcaldia') }}</span>

        <vs-input size="large" v-validate="'required'" label="Entidad Federativa" placeholder="Entidad Federativa" name="Entidad Federativa" v-model="form.entidadFederativa" class="mt-5 w-full" />
        <span class="text-danger text-sm" v-show="errors.has('EntidadFederativa')">{{ errors.first('Entidad Federativa') }}</span>

        <vs-input size="large" v-validate="'required'" label="Coordenadas" placeholder="Coordenadas" name="Coordenadas" v-model="form.coordenadas" class="mt-5 w-full" />
        <span class="text-danger text-sm" v-show="errors.has('Coordenadas')">{{ errors.first('Coordenadas') }}</span>

        <vs-input size="large" v-validate="'required'" label="Poblacion Cercana" placeholder="Poblacion Cercana" name="Poblacion Cercana" v-model="form.poblacionCercana" class="mt-5 w-full" />
        <span class="text-danger text-sm" v-show="errors.has('PoblacionCercana')">{{ errors.first('Poblacion Cercana') }}</span>

        <vs-input size="large" v-validate="'required'" label="Referencia" placeholder="Referencia" name="Referencia" v-model="form.referencia" class="mt-5 w-full" />
        <span class="text-danger text-sm" v-show="errors.has('Referencia')">{{ errors.first('Referencia') }}</span>

        <vs-button type="filled" @click.prevent="submitForm" class="mt-5 block">Guardar</vs-button>
      </form>
    </vs-popup>
</template>
<script>
// import servicio from '@/services/misiones/mantenimiento'
import servicio from '@/services/misiones/direccionM'

export default {
  components: {
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
      form: {
        calle: '',
        colonia: '',
        alcaldia: '',
        entidadFederativa: '',
        coordenadas: '',
        poblacionCercana: '',
        referencia: '',
        state: true,
        created_date: null

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
    borrar(){
        this.form.fechaInicio= null
        this.form.apellido1= null
        this.form.apellido2= null
        this.form.numeroEmpleado= null
        this.form.nombre= null
        this.form.state= null
    },
    submitForm() {
        this.$validator.validateAll().then(result => {
        const hoy = new Date();
        this.form.created_date = this.formatoFecha(hoy, 'yy-mm-dd')
        console.log('sssssss', result)
        if(result) {
          this.$vs.loading()
          // if form have no errors
          servicio.crear(this.form).then(response => {
            console.log(response)
            this.borrar()
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
<style type="text/css">
  .mensajeE {
    background-color: white;
    color: red;
    position: relative;
    bottom: 20px;
  }
</style>

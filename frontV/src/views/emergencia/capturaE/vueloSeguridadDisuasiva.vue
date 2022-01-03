<template>
    <vs-popup class="holamundo" title="Vuelo de seguridad disuasiva" :active.sync="verL">
      <form>
        
        
        <vs-input size="large" v-validate="'required'" label="Zona a volar" placeholder="Zona a volar" name="Zona a volar" v-model="form.zonaV" class="mt-5 w-full" />
        <span class="text-danger text-sm" v-show="errors.has('zonaV')">{{ errors.first('zonaV') }}</span>

        <vs-input size="large" v-validate="'required'" label="Delitos a inhibir" placeholder="Delitos a inhibir" name="Delitos a inhibir" v-model="form.delitoI" class="mt-5 w-full" />
        <span class="text-danger text-sm" v-show="errors.has('delitosI')">{{ errors.first('delitosI') }}</span>


        <vs-button type="filled" @click.prevent="submitForm" class="mt-5 block">Guardar</vs-button>
      </form>
    </vs-popup>
</template>
<script>


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
        zonaV: '',
        delitoI: ''

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
    submitForm(){
      console.log('envia formulario', this.form);

      this.$emit('formServicio', this.form)
      this.$emit('cerrar', this.form)
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

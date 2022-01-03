<template>
    <vs-popup class="holamundo" title="Apoyo a unidades en tierra " :active.sync="verL">
      <form>
        
        
        <vs-input size="large" v-validate="'required'" label="Nombre" placeholder="Nombre" name="Nombre" v-model="form.nombre" class="mt-5 w-full" />
        <span class="text-danger text-sm" v-show="errors.has('Nombre')">{{ errors.first('Nombre') }}</span>


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
        helicoptero: null,
        fechaInicio: null,
        apellido1: null,
        apellido2: null,
        numeroEmpleado: null,
        nombre: '',
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
    submitForm(){
      console.log('envia formulario', this.form);
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

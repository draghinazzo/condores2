<template>
    <vx-card title="Servicio Apoyo  Unidad Pie Tierra" id="parentx-demo-5">
      <form>
        
        
        <vs-input size="large" v-validate="'required'" label="Nombre" placeholder="Nombre" name="Nombre" v-model="form.nombre" class="mt-5 w-full" />
        <span class="text-danger text-sm" v-show="errors.has('Nombre')">{{ errors.first('Nombre') }}</span>

      </form>
    </vx-card>
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
  },

  methods: {
    submitForm(){
      console.log('envia formulario', this.form);
    }
  },
  watch: {
  },
  computed: {
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

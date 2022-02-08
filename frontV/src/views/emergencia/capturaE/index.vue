<template>
    <vx-card title="Emergencia" id="parentx-demo-5">
        <b-form @submit.stop.prevent="submitForm"> 
        <b-row class="p-2">
          <b-col lg="4" md="4" sm="12" class="mb-1">
            <b-form-group label="Nombre solicitante" label-for="NumEmp-input">
              <b-form-input
                id="numEmp"
                name="nombreSolicitante"
                v-validate="{ required: true, numeric: true }"
                v-model="form.nombreSolicitante"
                placeholder="Nombre solicitante"
              />
              <span class="text-danger text-sm"> {{ errors.first('nombreSolicitante') }} </span>
            </b-form-group>
          </b-col>
          
          <b-col lg="4" md="4" sm="12" class="mb-1">

            <b-form-group label="Cargo" label-for="NumEmp-input">
              <b-form-input
                id="numEmp"
                name="cargo"
                v-validate="{ required: true, numeric: true }"
                v-model="form.cargo"
                placeholder="Cargo"
              />
              <span class="text-danger text-sm"> {{ errors.first('cargo') }} </span>
            </b-form-group>
          </b-col>

          <b-col lg="4" md="4" sm="12" class="mb-1">

            <b-form-group label="Telefono del solicitante" label-for="NumEmp-input">
              <b-form-input
                id="numEmp"
                name="Telefono del solicitante"
                v-validate="{ required: true, numeric: true }"
                v-model="form.telefono"
                placeholder="telefono"
              />
              <span class="text-danger text-sm"> {{ errors.first('telefono') }} </span>
            </b-form-group>
          </b-col>
        </b-row>
          <br>
          <br>
        <b-row>
          <b-col lg="4" md="4" sm="12" class="mb-1">
            <label> Fecha y hora</label>
            <flat-pickr class="form-control" placeholder="Fecha y hora" v-model="form.fechaHora" :config="configdateTimePicker" />
            </b-col>
            <b-col lg="4" md="4" sm="12" class="mb-1">
              Medio
              <b-form-select  class="selectTa" v-model="selectMedio" :options="optionsMedio" :dir="$vs.rtl ? 'rtl' : 'ltr'" />     
            </b-col>   
            <b-col lg="4" md="4" sm="12" class="mb-1">
              Institucion
              <b-form-select  class="selectTa" v-model="selectInstitucion" :options="optionsInstitucion" :dir="$vs.rtl ? 'rtl' : 'ltr'" />     
            </b-col>   
        </b-row>
        <br>
        <br>
        <b-row>
          <b-col lg="3" md="3" sm="12" class="mb-1">
            Servicio
            <b-form-select class="selectTa" @input="abrirFormServicio" v-model="selectServicio" :options="optionsServicio" :dir="$vs.rtl ? 'rtl' : 'ltr'" />
           
          </b-col>   
            
        </b-row>
        <br><br>
        <b-row>
          <apoyoUT v-show="activeApoyoUT" :id="idE"  @cerrar="ocultarVentanaApoyoUT" @formServicio="formServicioA" ></apoyoUT>
          <ambulanciaA v-show="activeAmbulanciaA"  :id="idE"  @cerrar="ocultarVentanaAmbulanciaA" @formServicio="formServicioA"></ambulanciaA>
          <vueloSD v-show="activeVueloSD" :id="idE"  @cerrar="ocultarVentanaVueloSD" @formServicio="formServicioA"></vueloSD>
        </b-row>
        <vs-button type="filled" @click.prevent="submitForm" class="mt-5 block">Guardar</vs-button>
        
      </b-form>
    </vx-card>
</template>

<script>
import apoyoUT from'@/views/emergencia/capturaE/apoyoUnidadTierra.vue'
import ambulanciaA from'@/views/emergencia/capturaE/ambulanciaAerea.vue'
import vueloSD from'@/views/emergencia/capturaE/vueloSeguridadDisuasiva.vue'


import servicioI from '@/services/catalogos/institucion'
import Datepicker from 'vuejs-datepicker';
import flatPickr from 'vue-flatpickr-component';
import 'flatpickr/dist/flatpickr.css';
import {Spanish as espa} from 'flatpickr/dist/l10n/es.js';
import vSelect from 'vue-select'
// import direccionMServicio from '@/services/misiones/direccionM'
import medioServicio from '@/services/misiones/medio'
import servicioServicio from '@/services/misiones/servicio'

export default {
  components: {
    vueloSD,
    ambulanciaA,
    apoyoUT,
    Datepicker,
    flatPickr,
    'v-select': vSelect,
  },
  data() {
    return {
      idE: 0,
      activeVueloSD: false, 
      activeAmbulanciaA: false,
      activeApoyoUT: false,
      selectTipoE: {id:''},
      selectSexo: null,
      selectSolicitante: null,
      selectServicio: null,
      selectMedio: null,
      selectInstitucion: null,
      selecDireccion: null,
      selechelicoptero: null,
      queryPage: {
        limit: 10,
        offset: 0,
        nombre: ''
      },
      optionsTipoE: [],
      optionsSexo: [],
      optionsSolicitante: [],
      optionsServicio: [],
      optionsInstitucion: [],
      optionsHelicoptero: [],
      optionsMedio: [],
      mostrarM2: false,
      mostrarM: false,
      configdateTimePicker: {
        locale: espa
      },
      id: null,
      form: {
        json:'',
        fechaHora: '',
        cargo: '',
        nombreSolicitante: '',
        state: true,
        created_date:'2021-10-06',
      }
    }
  },
  mounted() {
    this.id = this.$route.params.id
    this.getInstituciones()
    this.getMedio()
    this.getServicio()
  },

  methods: {
    ocultarVentanaApoyoUT(){
      this.activeApoyoUT = false
      this.getDatos()
    },
    ocultarVentanaAmbulanciaA(){
      this.activeAmbulanciaA = false
      this.getDatos()
    },
    ocultarVentanaVueloSD(){
      this.activeVueloSD = false
      this.getDatos()
    },

    formServicioA(value){
      console.log('formmm', value);
      this.form.json = value
    },
    abrirFormServicio(){
      console.log('sss', this.selectServicio);
      if(this.selectServicio=== 1){
        
        this.activeVueloSD = true

        this.activeAmbulanciaA = false
        this.activeApoyoUT = false

      }if(this.selectServicio=== 3){
        this.activeAmbulanciaA = true
        
        this.activeVueloSD = false
        this.activeApoyoUT = false

      }if(this.selectServicio=== 2){
        this.activeApoyoUT = true

        this.activeAmbulanciaA = false
        this.activeVueloSD = false

      }
    },
    getServicio(){
      servicioServicio.select(this.queryPage)
        .then(response => {
          this.$vs.loading.close()
          this.optionsServicio= response.data.results
        })
        .catch(error => {
          
          this.$vs.loading.close()
          console.log(error)
          })
    },
    getMedio(){
      medioServicio.select(this.queryPage)
        .then(response => {
          this.$vs.loading.close()
          this.optionsMedio= response.data.results
          console.log('mediooo', this.optionsMedio)
        })
        .catch(error => {
          
          this.$vs.loading.close()
          console.log(error)
          })
    },
    getInstituciones(){
      servicioI.select(this.queryPage)
        .then(response => {
          this.$vs.loading.close()
          this.optionsInstitucion = response.data.results
        })
        .catch(error => {
          
          this.$vs.loading.close()
          console.log(error)
          })
    },
    getDatos(){
      console.log('getDatos');
    },
    formatoFecha(fecha, formato) {
      const map = {
          dd: ("0" + fecha.getDate()).slice(-2),
          mm:("0" + (fecha.getMonth() + 1)).slice(-2),
          yy: fecha.getFullYear()
      }
      return formato.replace(/dd|mm|yy|yyy/gi, matched => map[matched])
    },
    submitForm() {
      console.log('envia datos', this.form)
    }
  },
  watch: {
  },
  computed: {
  }
}
</script>
<style lang="scss">
  .espacio {
  margin-left: 50%;

  }

  .selectTa {
    display:block;
    height:40px;
    width: 200px;
  }
</style>
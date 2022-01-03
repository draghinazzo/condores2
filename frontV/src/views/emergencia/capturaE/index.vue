<template>
    <vx-card title="Emergencia" id="parentx-demo-5">
        <form>
        <vs-row>
          <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="4" vs-sm="4" vs-xs="12" >
            <vs-input size="large" v-validate="'required'" label="Nombre solicitante"  placeholder="Nombre solicitante" name="Nombre solicitante" v-model="form.nombreSolicitante" class="mt-5 w-full" />
            <span class="text-danger text-sm" v-show="errors.has('nombreSolicitante')">{{ errors.first('nombreSolicitante') }}</span>
          </vs-col>
          
          <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="4" vs-sm="4" vs-xs="12" >
            <vs-input size="large" v-validate="'required'" label="Cargo"  placeholder="Cargo" name="Cargo" v-model="form.cargo" class="mt-5 w-full" />
            <span class="text-danger text-sm" v-show="errors.has('cargo')">{{ errors.first('cargo') }}</span>
          </vs-col>

          <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="4" vs-sm="4" vs-xs="12" >
            <vs-input size="large" v-validate="'required'" label="Telefono del solicitante"  placeholder="Telefono del solicitante" name="Telefono del solicitante" v-model="form.telefono" class="mt-5 w-full" />
            <span class="text-danger text-sm" v-show="errors.has('telefono')">{{ errors.first('telefono') }}</span>
          </vs-col>
        </vs-row>
          <br>
          <br>
        <vs-row>
          <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="4" vs-sm="4" vs-xs="12" >
            <label> Fecha y hora</label>
            <flat-pickr placeholder="Fecha y hora" v-model="form.fechaHora" :config="configdateTimePicker" />
            </vs-col>
            <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="4" vs-sm="4" vs-xs="12" >
              Medio
              <v-select  class="selectTa" v-model="selectMedio" :options="optionsMedio" :dir="$vs.rtl ? 'rtl' : 'ltr'" />     
            </vs-col>   
            <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="4" vs-sm="4" vs-xs="12" >
              Institucion
              <v-select  class="selectTa" v-model="selectInstitucion" :options="optionsInstitucion" :dir="$vs.rtl ? 'rtl' : 'ltr'" />     
            </vs-col>   
        </vs-row>
        <br>
        <br>
        <vs-row>
          <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="12" vs-sm="12" vs-xs="12" >
            Servicio
            <v-select class="selectTa" v-model="selectServicio" :options="optionsServicio" :dir="$vs.rtl ? 'rtl' : 'ltr'" />
            <vs-button type="border" size="small" icon-pack="feather" @click="abrirFormServicio()" icon="icon-search" color="danger"></vs-button>
          </vs-col>  
        </vs-row>
        <apoyoUT :id="idE" :ver="activeApoyoUT" @cerrar="ocultarVentanaApoyoUT" @formServicio="formServicioA" ></apoyoUT>
        <ambulanciaA :id="idE" :ver="activeAmbulanciaA" @cerrar="ocultarVentanaAmbulanciaA" @formServicio="formServicioA"></ambulanciaA>
        <vueloSD :id="idE" :ver="activeVueloSD" @cerrar="ocultarVentanaVueloSD" @formServicio="formServicioA"></vueloSD>

        <vs-button type="filled" @click.prevent="submitForm" class="mt-5 block">Guardar</vs-button>
        
      </form>
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
    },
    abrirFormServicio(){
      if(this.selectServicio.id === 1){
        this.activeApoyoUT = true
      }if(this.selectServicio.id === 2){
        this.activeAmbulanciaA = true
      }if(this.selectServicio.id === 3){
        this.activeVueloSD = true
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
      console.log('envia datos')
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
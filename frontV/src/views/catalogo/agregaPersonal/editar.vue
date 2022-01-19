<template>
  <div>
    <vx-card title="Editar" id="parentx-demo-5">
      <b-row class="p-2">
        <b-col lg="8" md="8" sm="12" class="mb-1">
          
        </b-col>
        <b-col v-if="imagen != ''">
          <b-img
            class="imgRedonda"
            rounded="circle"
            :src="`data:image/png;base64, ${imagen}`"
          />
        </b-col>
      </b-row>
      <br>
      <b-row class="p-2">
        <b-col lg="4" md="4" sm="12" class="mb-1">
          <b-form-group label="Numero Empleado" label-for="NumEmp-input">
            <b-form-input
              id="numEmp"
              v-on:blur="consularN"
              v-model="form.numeroEmpleado"
              placeholder="Numero Empleado"
            />
          </b-form-group>
        </b-col>
        <b-col lg="4" md="4" sm="12" class="mb-1">
          <b-form-group label="Nombre" label-for="Nombre-input">
            <b-form-input
              id="nameEmp"
              
              v-model="form.nombre"
              placeholder="Nombre"
            />
          </b-form-group>
        </b-col>
      </b-row>
      <!-- Datos Nombre -->
      <b-row class="p-2">
        
        <b-col lg="4" md="4" sm="12" class="mb-1">
          <b-form-group label="Apellido 1" label-for="Apellido1-input">
            <b-form-input
              id="lastFEmp"
              
              v-model="form.apellido1"
              placeholder="Apellido Paterno"
            />
          </b-form-group>
        </b-col>
        <b-col lg="4" md="4" sm="12" class="mb-1">
          <b-form-group label="Apellido 2" label-for="Apellido2-input">
            <b-form-input
              id="lastSEmp"
              
              v-model="form.apellido2"
              placeholder="Apellido Materno"
            />
          </b-form-group>
        </b-col>
      </b-row>
      <!-- Datos Unicos Persona -->
      <b-row class="p-2">
        <b-col lg="4" md="4" sm="12" class="mb-1">
          <b-form-group label="CUIP" label-for="CUIP-input">
            <b-form-input
              id="nameEmp"
              
              v-model="form.cuip"
              placeholder="CUIP"
            />
          </b-form-group>
        </b-col>
        <b-col lg="4" md="4" sm="12" class="mb-1">
          <b-form-group label="RFC" label-for="RFC-input">
            <b-form-input
              id="lastFEmp"
              
              v-model="form.rfc"
              placeholder="RFC"
            />
          </b-form-group>
        </b-col>
        <b-col lg="4" md="4" sm="12" class="mb-1">
          <b-form-group label="CURP" label-for="CURP-input">
            <b-form-input
              id="lastSEmp"
              
              v-model="form.curp"
              placeholder="CURP"
            />
          </b-form-group>
        </b-col>
      </b-row>
      <!-- Datos Persona Mix-->
      <b-row class="p-2">
        <b-col b-col lg="3" md="3" sm="12" class="mb-1">
          <b-form-group label="Fecha de nacimiento" label-for="fechaN-input">
            <b-form-datepicker
              id="dateSEmp"
              
              class="mb-1"
              v-model="form.fechaNacimiento"
              placeholder="Fecha Nacimiento"
            />
          </b-form-group>
        </b-col>
        <b-col b-col lg="3" md="3" sm="12" class="mb-1">
          <b-form-group label="Excolaridad" label-for="Excolaridad-input">
            <b-form-input
              id="dateSEmp"
              v-validate="'required'"
              v-model="form.escolaridad"
              placeholder="Escolaridad"
            />
          </b-form-group>
        </b-col>
        <b-col>
          <b-form-group label="Adscripcion" label-for="Adscripcion-input">
            <b-form-input
              id="dateSEmp"
              
              v-model="form.adscripcion_general"
              placeholder="Adscripción"
            />
          </b-form-group>
        </b-col>
      </b-row>
      <!-- Datos Persona Mix2-->
      <b-row class="p-2">
        <b-col b-col lg="2" md="4" sm="12" class="mb-1">
          <b-form-group label="Grado" label-for="Grado-input">
            <b-form-input
              id="dateSEmp"
              
              v-model="form.grado"
              placeholder="Grado"
            />
          </b-form-group>
        </b-col>
        <b-col b-col lg="2" md="4" sm="12" class="mb-1">
          <b-form-group label="Antiguedad" label-for="Antiguedad-input">
            <b-form-input
              id="dateSEmp"
              
              v-model="form.antiguedad"
              placeholder="Antiguedad"
            />
          </b-form-group>
        </b-col>
        <b-col b-col lg="1" md="4" sm="12" class="mb-1">
          <b-form-group label="Edad" label-for="Edad-input">
            <b-form-input
              id="dateSEmp"
              
              v-model="form.edad"
              placeholder="Edad"
            />
          </b-form-group>
        </b-col>
        <b-col b-col lg="4" md="4" sm="12" class="mb-1">
          <b-form-group label="Capacidades" label-for="Capacidades-input">
            <b-form-input
              id="dateSEmp"
              
              v-model="form.capacidad"
              placeholder="Capacidades"
            />
          </b-form-group>
        </b-col>
        <b-col b-col lg="3" md="4" sm="12" class="mb-1">
          <b-form-group label="Descripcion" label-for="Descripcion-input">
            <b-form-input
              id="dateSEmp"
              
              v-model="form.descripcion"
              placeholder="Descripcion"
            />
          </b-form-group>
        </b-col>
      </b-row>
      <!-- Datos de contacto -->
      <b-row class="p-2">
        <b-col lg="3" md="4" sm="12" class="mb-1">
          <b-form-group label="Telefono Local" label-for="TelefonoL-input">
            <b-form-input
              id="PhoneLEmp"
              v-model="form.telefono"
              placeholder="Telefono Local"
            />
          </b-form-group>
        </b-col>
        <b-col lg="3" md="4" sm="12" class="mb-1">
          <b-form-group label="Telefono Celular" label-for="TelefonoC-input">
            <b-form-input
              id="PhoneMEmp"
              v-model="form.telefono_celular"
              placeholder="Telefono Celular"
            />
          </b-form-group>
        </b-col>
        <b-col lg="3" md="4" sm="12" class="mb-1">
          <b-form-group label="Telefono Oficina" label-for="TelefonoO-input">
          <b-form-input
            id="PhoneOEmp"
            v-model="form.telefono_oficina"
            placeholder="Telefono Oficina"
          />
          </b-form-group>
        </b-col>
        <b-col lg="3" md="4" sm="12" class="mb-1">
          <b-form-group label="Extension" label-for="Ext-input">
          <b-form-input
            id="PhoneExtEmp"
            v-model="form.extension"
            placeholder="Ext"
          />
          </b-form-group>
        </b-col>
      </b-row>
      <!-- Contacto Digital -->
      <b-row class="p-2">
        <b-col lg="3" md="4" sm="12" class="mb-1">
          <b-form-select
            
            v-model="selectSexo"
            :options="optionsSexo"
            size="sm"
            class="mt-1"
          />
        </b-col>
        <b-col lg="3" md="4" sm="12" class="mb-1">
          <b-form-select
            v-model="selectTipoE"
            :options="optionsTipoE"
            size="sm"
            class="mt-1"
          />
        </b-col>
        <b-col lg="3" md="4" sm="12" class="mb-1">
          <b-form-input
            id="EmailEmp"
            type="email"
            v-model="form.correo"
            placeholder="Correo Electronico"
          />
        </b-col>
        <b-col>
          <b-form-checkbox
            id="checkbox-1"
            v-model="form.esInstructor"
            name="checkbox-1"
            value="A"
            unchecked-value="not_accepted"
          >
            El Empleado es instructor
          </b-form-checkbox>
        </b-col>
      </b-row>
            <!-- Datos Piloto -->
      <b-row class="p-2">
        <b-col lg="3" md="4" sm="12" class="mb-1">
          <b-form-group label="Numero de Licencia" label-for="NumeroL-input">
            <b-form-input
              id="dateSEmp"
              
              v-model="form.numeroLicencia"
              placeholder="Numero de Licencia"
            />
          </b-form-group>
        </b-col>
        <b-col lg="3" md="4" sm="12" class="mb-1">
          <b-form-group label="Tipo de licencia" label-for="TipoL-input">
            <b-form-input
              id="dateSEmp"
              
              v-model="form.tipoLicencia"
              placeholder="Tipo de licencia"
            />
          </b-form-group>
        </b-col>
        <b-col lg="3" md="4" sm="12" class="mb-1">
          <b-form-group label="Vigencia de licencia" label-for="Vigencia-input">
            <b-form-datepicker
              id="vigencia"
              v-model="form.vigencia"
              placeholder="Vigencia de licencia"
              class="mb-1"
            />
          </b-form-group>
        </b-col>
        
        <b-button type="filled" @click.prevent="submitForm" class="mt-5 block">
          Guardar
        </b-button>
      </b-row>
    </vx-card>
  </div>
</template>

<script>
import consultaEmpleadoServicio from "@/services/consultaEmpleado";
import tipoEServicio from "@/services/misiones/tipoE";
import sexoServicio from "@/services/misiones/sexo";
import servicioPersona from '@/services/catalogos/persona'


import vSelect from "vue-select";
import Datepicker from "vuejs-datepicker";
import flatPickr from "vue-flatpickr-component";
import "flatpickr/dist/flatpickr.css";
import { Spanish as espa } from "flatpickr/dist/l10n/es.js";
import { BFormSelect } from 'bootstrap-vue'

export default {
  components: {
    BFormSelect,
    Datepicker,
    flatPickr,
    "v-select": vSelect,
  },
  data() {
    return {
      id: null,
      created_date: "2021-10-06",
      configdateTimePicker: {
        locale: espa,
      },
      selectSexo: 2,
      optionsSexo: [],
      optionsTipoE: [],
      imagen: "",
      selectTipoE: 1,
      form: {
        antiguedad: '',
        esInstructor: true,
        vigencia: null,
        capacidad: null,
        numeroEmpleado: '',
        nombre: '',
        apellido1: '',
        apellido2: '',
        curp: '',
        rfc: '',
        cuip: '',
        grado: '',
        telefono: '',
        telefono_oficina: '',
        extension: '',
        telefono_celular: '',
        adscripcion_general: '',
        correo: '',
        descripcion: '',
        escolaridad: '',
        edad: '',
        fechaNacimiento: '',
        numeroLicencia: null,
        tipoLicencia: null,
        tipo_empleado: '',
        sexo: '',
        //colonia: '',
        //alcaldia: '',
        //municipio: '',
        //entidadFederativa: '',
        //codigoPostal: '',
        state: true,
        created_date:'2021-10-06'

      },
      queryPage: {
        limit: 10,
        offset: 0,
        nombre: "",
      },
    };
  },
  mounted() {
    this.id = this.$route.params.id
    this.getTipoE();
    this.getSexo();
    this.getDatos();
  },

  methods: {
    getSexo() {
      sexoServicio
        .select(this.queryPage)
        .then((response) => {
          this.$vs.loading.close();
          console.log(response.data.results)
          this.optionsSexo = response.data.results;
        })
        .catch((error) => {
          this.$vs.loading.close();
          console.log(error);
        });
    },
    getTipoE() {
      tipoEServicio
        .select(this.queryPage)
        .then((response) => {
          this.$vs.loading.close();
          this.optionsTipoE = response.data.results;
        })
        .catch((error) => {
          this.$vs.loading.close();
          console.log(error);
        });
    },
    getDatos() {
      servicioPersona
        .obtenerId(this.id)
        .then((response) => {
          
          this.$vs.loading();
          console.log('editar', response.data)
          this.form.curp = response.data.curp
          this.form.nombre = response.data.nombre
          this.form.numeroEmpleado = response.data.numeroEmpleado
          this.form.apellido1 = response.data.apellido1
          this.form.apellido2 = response.data.apellido2
          this.form.cuip = response.data.cuip
          this.form.rfc = response.data.rfc
          this.form.fechaNacimiento = response.data.fechaNacimiento
          this.form.escolaridad = response.data.escolaridad
          this.form.adscripcion_general = response.data.adscripcion_general
          this.form.grado = response.data.grado
          this.form.antiguedad = response.data.antiguedad
          this.form.edad = response.data.edad
          this.form.capacidad = response.data.capacidad
          this.form.descripcion = response.data.descripcion
          this.form.telefono = response.data.telefono
          this.form.telefono_celular = response.data.telefono_celular
          this.form.telefono_oficina = response.data.telefono_oficina
          this.form.correo = response.data.correo
          this.form.esInstructor = response.data.esInstructor
          if(this.form.esInstructor === true){
            this.form.esInstructor = ['A']
          }
          this.form.numeroLicencia = response.data.numeroLicencia
          this.form.tipoLicencia = response.data.tipoLicencia
          this.form.vigencia = response.data.vigencia
          this.form.extension = response.data.extension
          this.selectSexo = response.data.sexoID
          this.selectTipoE = response.data.tipoEmpleadoId
          consultaEmpleadoServicio
          .consultarImagen(this.form.numeroEmpleado)
          .then((response) => {
            this.imagen = response.data.data[0].data.imagen;
            
            this.$vs.loading.close();
          })
          .catch((error) => {
            this.$vs.loading.close();
            console.log(error);
          })
        })
        .catch((error) => {
          this.$vs.loading.close();
          console.log(error);
        });
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
      this.form.sexo = this.selectSexo.id
      this.form.tipo_empleado = this.selectTipoE.id
      console.log('form', this.form);
      if (this.form.esInstructor !== true ){
        this.form.esInstructor = false
      }
      this.$validator.validateAll().then(result => {
        this.$vs.loading()
        const hoy = new Date();
        this.form.modified_date = this.formatoFecha(hoy, 'yy-mm-dd')
        if(result) {

          // if form have no errors
          servicioPersona.actualizarId(this.id, this.form).then(response => {
            console.log('response', response)
            this.$vs.loading.close()
          })
          .catch(error => console.log(error))
        }else{
          this.$vs.loading.close()
          console.log('eeeee', result);
          // form have errors
          
         }
      })
    },
    consularN() {
      this.mostrarM = false;
      this.mostrarM2 = false;
      if (isNaN(this.form.numeroEmpleado) || this.form.numeroEmpleado < 1) {
        this.$vs.notify({
          title: "Error",
          text: "Error en la placa escrita",
          color: "danger",
        });
      } else {
        this.$vs.loading();
        consultaEmpleadoServicio
          .consultarImagen(this.form.numeroEmpleado)
          .then((response) => {
            this.imagen = response.data.data[0].data.imagen;
            consultaEmpleadoServicio
              .consultarEmpleado(this.form.numeroEmpleado)
              .then((response) => {
                console.log(
                  "response.data.data[0].data",
                  response.data.data[0].data
                );
                this.form.nombre = response.data.data[0].data.nombre;
                this.form.apellido1 = response.data.data[0].data.primer_apellido;
                this.form.apellido2 = response.data.data[0].data.segundo_apellido;
                this.form.curp = response.data.data[0].data.curp;
                this.form.rfc = response.data.data[0].data.rfc;
                this.form.cuip = response.data.data[0].data.cuip;
                this.form.grado = response.data.data[0].data.grado;
                this.form.telefono = response.data.data[0].data.telefono;
                this.form.telefono_oficina = response.data.data[0].data.telefono_oficina;
                this.form.extension = response.data.data[0].data.extension;
                this.form.telefono_celular = response.data.data[0].data.telefono_celular;
                this.form.adscripcion_general = response.data.data[0].data.adscripcion_general;
                this.form.correo = response.data.data[0].data.correo;
                this.form.descripcion = response.data.data[0].data.descripcion;
                this.form.escolaridad = response.data.data[0].data.escolaridad;
                this.form.edad = response.data.data[0].data.edad;
                this.form.antiguedad = response.data.data[0].data.antiguedad;
                this.form.fechaNacimiento = response.data.data[0].data.fecha_nacimiento;
                this.selectSexo = response.data.data[0].data.sexo
                this.$vs.loading.close();
              })
              .catch((error) => {
                this.$vs.loading.close();
                console.log(error);
              });
          })
          .catch((error) => {
            this.$vs.loading.close();
            console.log(error);
          });
      }
    },
  },
  watch: {},
  computed: {},
};
</script>
<style lang="scss">
@media only screen and (min-width: 100px)  and (max-width : 767px){
  .imgRedonda {
    width: 150px;
    height: 150px;
    border-radius: 150px;
  }
}
@media only screen and (min-width: 701px) and (max-width : 1700px){
  .imgRedonda {
    width: 150px;
    height: 150px;
    border-radius: 150px;
    float: right;
    position: absolute;
    margin-left: 10%;
  }
}
.espacio {
  margin-left: 50%;
}

.foto {
  display: block;
  height: 150px;
  width: 120px;
}
</style>

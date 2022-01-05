<template>
  <div>
    <vx-card title="Agregar Personal" id="parentx-demo-5">
      <b-row class="p-2">
        <b-col lg="8" md="8" sm="12" class="mb-1">
          <b-form-group label="Numero Empleado" label-for="NumEmp-input">
            <b-form-input
              id="numEmp"
              v-on:blur="consularN"
              v-model="form.numeroEmpleado"
              placeholder="Numero Empleado"
            />
          </b-form-group>
        </b-col>
        <b-col v-if="imagen != ''">
          <b-img
            class="imgRedonda"
            rounded="circle"
            :src="`data:image/png;base64, ${imagen}`"
          />
        </b-col>
      </b-row>
      <!-- Datos Nombre -->
      <b-row class="p-2">
        <b-col lg="4" md="4" sm="12" class="mb-1">
          <b-form-input
            id="nameEmp"
            :disabled="true"
            v-model="form.nombre"
            placeholder="Nombre"
          />
        </b-col>
        <b-col lg="4" md="4" sm="12" class="mb-1">
          <b-form-input
            id="lastFEmp"
            :disabled="true"
            v-model="form.apellido1"
            placeholder="Apellido Paterno"
          />
        </b-col>
        <b-col lg="4" md="4" sm="12" class="mb-1">
          <b-form-input
            id="lastSEmp"
            :disabled="true"
            v-model="form.apellido2"
            placeholder="Apellido Materno"
          />
        </b-col>
      </b-row>
      <!-- Datos Unicos Persona -->
      <b-row class="p-2">
        <b-col lg="4" md="4" sm="12" class="mb-1">
          <b-form-input
            id="nameEmp"
            :disabled="true"
            v-model="form.cuip"
            placeholder="CUIP"
          />
        </b-col>
        <b-col lg="4" md="4" sm="12" class="mb-1">
          <b-form-input
            id="lastFEmp"
            :disabled="true"
            v-model="form.rfc"
            placeholder="RFC"
          />
        </b-col>
        <b-col lg="4" md="4" sm="12" class="mb-1">
          <b-form-input
            id="lastSEmp"
            :disabled="true"
            v-model="form.curp"
            placeholder="CURP"
          />
        </b-col>
      </b-row>
      <!-- Datos Persona Mix-->
      <b-row class="p-2">
        <b-col b-col lg="2" md="4" sm="12" class="mb-1">
          <b-form-input
            id="dateSEmp"
            :disabled="true"
            v-model="form.fechaNacimiento"
            placeholder="Fecha Nacimiento"
          />
        </b-col>
        <b-col b-col lg="2" md="4" sm="12" class="mb-1">
          <b-form-input
            id="dateSEmp"
            :disabled="true"
            v-model="form.sexo"
            placeholder="Sexo"
          />
        </b-col>
        <b-col>
          <b-form-input
            id="dateSEmp"
            :disabled="true"
            v-model="form.adscripcion_general"
            placeholder="Adscripción"
          />
        </b-col>
      </b-row>
      <!-- Datos de contacto -->
      <b-row class="p-2">
        <b-col lg="3" md="4" sm="12" class="mb-1">
          <b-form-input
            id="PhoneLEmp"
            v-model="form.telefono"
            placeholder="Telefono Local"
          />
        </b-col>
        <b-col lg="3" md="4" sm="12" class="mb-1">
          <b-form-input
            id="PhoneMEmp"
            v-model="form.telefono_celular"
            placeholder="Telefono Celular"
          />
        </b-col>
        <b-col lg="3" md="4" sm="12" class="mb-1">
          <b-form-input
            id="PhoneOEmp"
            v-model="form.telefono_oficina"
            placeholder="Telefono Oficina"
          />
        </b-col>
        <b-col lg="3" md="4" sm="12" class="mb-1">
          <b-form-input
            id="PhoneExtEmp"
            v-model="form.extencion"
            placeholder="Ext"
          />
        </b-col>
      </b-row>
      <!-- Contacto Digital -->
      <b-row class="p-2">
        <b-col lg="3" md="4" sm="12" class="mb-1">
          <b-form-input
            id="EmailEmp"
            type="email"
            v-model="form.email"
            placeholder="Correo Electronico"
          />
        </b-col>
        <b-col>
          <b-form-checkbox
            id="checkbox-1"
            v-model="form.esInstructor"
            name="checkbox-1"
            value="accepted"
            unchecked-value="not_accepted"
          >
            El Empleado es instructor
          </b-form-checkbox>
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

import vSelect from "vue-select";
import Datepicker from "vuejs-datepicker";
import flatPickr from "vue-flatpickr-component";
import "flatpickr/dist/flatpickr.css";
import { Spanish as espa } from "flatpickr/dist/l10n/es.js";
export default {
  components: {
    Datepicker,
    flatPickr,
    "v-select": vSelect,
  },
  data() {
    return {
      created_date: "2021-10-06",
      configdateTimePicker: {
        locale: espa,
      },
      selectSexo: null,
      optionsSexo: [],
      optionsTipoE: [],
      imagen: "",
      selectTipoE: null,
      form: {
        antiguedad: '',
        esInstructor:'',
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
    this.getTipoE();
    this.getSexo();
  },

  methods: {
    getSexo() {
      sexoServicio
        .select(this.queryPage)
        .then((response) => {
          this.$vs.loading.close();
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
    submitForm() {
      console.log("enviar");
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
                this.form.extencion = response.data.data[0].data.extension;
                this.form.telefono_celular = response.data.data[0].data.telefono_celular;
                this.form.adscripcion_general = response.data.data[0].data.adscripcion_general;
                this.form.correo = response.data.data[0].data.correo;
                this.form.descripcion = response.data.data[0].data.descripcion;
                this.form.escolaridad = response.data.data[0].data.escolaridad;
                this.form.edad = response.data.data[0].data.edad;
                this.form.fechaNacimiento =
                  response.data.data[0].data.fecha_nacimiento;

                var label;
                response.data.data[0].data.sexo === 1
                  ? (label = "Masculino")
                  : (label = "Femenino");
                this.selectSexo = {
                  id: response.data.data[0].data.sexo,
                  label: label,
                };
                var label2;
                response.data.data[0].data.tipo_empleado === 1
                  ? (label2 = "Policia")
                  : (label2 = "Administrativo");
                this.selectTipoE = {
                  id: response.data.data[0].data.tipo_empleado,
                  label: label2,
                };

                if (response.data.data[0].error === 1) {
                  this.$vs.notify({
                    title: "Error",
                    text: "La placa no existe2",
                    color: "danger",
                  });
                }
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
.imgRedonda {
  width: 150px;
  height: 150px;
  border-radius: 150px;
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

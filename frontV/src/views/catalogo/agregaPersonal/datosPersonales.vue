<template>
    <vx-card title="Datos personales" id="parentx-demo-5">
        <vs-row vs-align="flex-end"
                vs-type="flex" 
                vs-justify="space-between" vs-w="12">
            <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="3">
                <vs-input size="large" v-validate="'required'" label="Nombre" placeholder="Nombre" name="Nombre" v-model="form.nombre" class="mt-5 w-full" />
                <span class="text-danger text-sm" v-show="errors.has('Nombre')">{{ errors.first('Nombre') }}</span>
            </vs-col>    
            <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="3">
                <vs-input size="large" v-validate="'required'" label="Apellido1" placeholder="Apellido1" name="Apellido1" v-model="form.apellido1" class="mt-5 w-full" />
                <span class="text-danger text-sm" v-show="errors.has('Apellido1')">{{ errors.first('Apellido1') }}</span>
            </vs-col>    
            <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="3">
                <vs-input size="large" v-validate="'required'" label="Apellido2" placeholder="Apellido2" name="Apellido2" v-model="form.apellido2" class="mt-5 w-full" />
                <span class="text-danger text-sm" v-show="errors.has('Apellido2')">{{ errors.first('Apellido2') }}</span>
            </vs-col>
        </vs-row>
        <vs-row vs-align="flex-end"
                vs-type="flex" 
                vs-justify="space-between" vs-w="12">
            <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="3">
                <vs-input size="large" v-validate="'required'" label="CURP" placeholder="CURP" name="CURP" v-model="form.curp" class="mt-5 w-full" />
                <span class="text-danger text-sm" v-show="errors.has('CURP')">{{ errors.first('CURP') }}</span>
             </vs-col>    
            <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="3">
                <vs-input size="large" v-validate="'required'" label="RFC" placeholder="RFC" name="RFC" v-model="form.rfc" class="mt-5 w-full" />
                <span class="text-danger text-sm" v-show="errors.has('RFC')">{{ errors.first('RFC') }}</span>
            </vs-col>    
            <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="3">
                <vs-input size="large" v-validate="'required'" label="CUIP" placeholder="CUIP" name="CUIP" v-model="form.cuip" class="mt-5 w-full" />
                <span class="text-danger text-sm" v-show="errors.has('CUIP')">{{ errors.first('CUIP') }}</span>
            </vs-col>
        </vs-row>
    </vx-card>
</template>

<script>

export default {
  components: {
  },
  data() {
    return {
      form: {
        nombre: '',
        apellido1: '',
        apellido2: '',
        curp: '',
        rfc: '',
        cuip: '',
        state: true,
        created_date:'2021-10-06'

      }
    }
  },
  mounted() {
  },

  methods: {
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
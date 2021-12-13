<template>
      <vx-card title="Cursos" code-toggler id="parentx-demo-5">

      <vs-button @click="abrirFormulario" color="primary" type="filled">Agregar nuevo registro</vs-button>

      <formulario :ver="active" @cerrar="ocultarVentana" ></formulario>
      <editar :id="idE" :ver="activeEditar" @cerrar="ocultarVentanaEditar" ></editar>

        <vs-table :sst="true" :max-items="10" search @search="handleSearch" :data="medio">
            <template slot="thead">
                <vs-th sort-key="email">id</vs-th>
                <vs-th sort-key="username">Nombre del curso</vs-th>
                <vs-th sort-key="username">Fecha de inicio</vs-th>
                <vs-th sort-key="username">Fecha termino</vs-th>
                <vs-th sort-key="username">Instructor</vs-th>
            </template>

            <template slot-scope="{data}">
                <vs-tr :key="indextr" v-for="(tr, indextr) in data">

                    <vs-td :data="data[indextr].id">
                        {{data[indextr].id}}
                    </vs-td>

                    <vs-td :data="data[indextr].nombreCurso">
                        {{data[indextr].nombreCurso}}
                    </vs-td>

                    <vs-td :data="data[indextr].fechaInicio">
                        {{data[indextr].fechaInicio}}
                    </vs-td>
                    
                    <vs-td :data="data[indextr].fechaFin">
                        {{data[indextr].fechaFin}}
                    </vs-td>
                    
                    <vs-td :data="data[indextr].instructorNombre">
                        {{data[indextr].instructorNombre}}
                        {{data[indextr].instructorApellido1}}
                        {{data[indextr].instructorApellido2}}
                    </vs-td>

                    <vs-td :data="data[indextr].id">
                        <div class="flex">
                          <vs-button type="border" size="small" icon-pack="feather" @click="abrirEditar(data[indextr].id)" icon="icon-search" color="success" class="mr-2"></vs-button>
                          <vs-button type="border" size="small" icon-pack="feather" @click="eliminar(data[indextr].id)" icon="icon-trash" color="danger"></vs-button>
                        </div>
                    </vs-td>

                    
                </vs-tr>
                <vs-row>
                    <vs-col vs-offset="10" vs-type="flex" vs-justify="center" vs-align="center" vs-w="2" class="sm:p-2 p-4">
                        <vs-pagination :total="totalPaginas" v-model="currentx"> </vs-pagination>
                    </vs-col>
                </vs-row>
            </template>
        </vs-table>
      </vx-card>
</template>
<script>
import servicio from '@/services/capacitacion/curso'
import formulario from'@/views/capacitacion/Cursos/formulario.vue'
import editar from'@/views/capacitacion/Cursos/editar.vue'


export default {
  components: {
    formulario,
    editar
  },
  data() {
    return {
      idE: 0,
      activeEditar: false,
      active: false,
      buscar:'',
      medio: '',
      currentx: 1,
      totalPaginas: 1,
      queryPage: {
        limit: 10,
        offset: 0,
        nombre: ''
      }
    }
  },
  mounted() {
    this.getDatos()
  },
  methods: {
    ocultarVentanaEditar(){
      this.activeEditar = false
      this.getDatos()
    },
    abrirEditar(id){
      this.idE = id
      this.activeEditar = true
      // this.$router.push({ name: 'editarMision', params: {id:id} })
    },
    eliminar(id){
      this.$vs.loading()
      servicio.eliminar(id).then(response => {
          this.getDatos()
          this.$vs.loading.close()
          console.log(response)
        })
        .catch(error => {
          console.log(error);
          this.$vs.loading.close()
        })
      },
    ocultarVentana(){
      this.active = false
      this.getDatos()
    },
    abrirFormulario(){
      this. active = true
      // this.$router.push({ name: 'guardarMision' })
    },
     handleSearch(searching) {
      this.queryPage.nombre = searching
      this.getDatos()
    },
    pagina(){
      console.log('paginaaa', this.currentx)
    },
    getDatos() {
      this.$vs.loading()
      // const vm = this
      servicio.obtener(this.queryPage)
        .then(response => {
          console.log('misionesss', response.data.results)
          this.$vs.loading.close()
          this.medio = response.data.results
          this.totalPaginas = Math.ceil(response.data.count / 10)

        })
        .catch(error => {
          
          this.$vs.loading.close()
          console.log(error)
          })
    },
  },
  watch: {
    buscar(){
      console.log('sasas', this.buscar)
    },
    currentx () {
      let paginas = []
      for (let index = 0; index < this.totalPaginas; index++) {// lleno un arreglo para tomar la pagina del valor que envia el paginador
        paginas.push(index*10)
      }
      this.queryPage.offset=paginas[this.currentx-1]
      this.getDatos()
    }
  }
}
</script>

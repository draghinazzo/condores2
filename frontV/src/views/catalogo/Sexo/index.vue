<template>
      <vx-card title="Sexo" code-toggler id="parentx-demo-5">

      <vs-button @click="abrirFormulario" color="primary" type="filled">Agregar nuevo registro</vs-button>
      <formulario :ver="active" @cerrar="ocultarVentana" ></formulario>
      <editar :id="idE" :ver="activeEditar" @cerrar="ocultarVentanaEditar" ></editar>

        <vs-table :sst="true" :max-items="10" search @search="handleSearch" :data="medio">
            <template slot="thead">
                <vs-th sort-key="email">id</vs-th>
                <vs-th sort-key="username">Sexo</vs-th>
                <vs-th sort-key="username">Acciones</vs-th>
            </template>

            <template slot-scope="{data}">
                <vs-tr :key="indextr" v-for="(tr, indextr) in data">

                    <vs-td :data="data[indextr].id">
                        {{data[indextr].id}}
                    </vs-td>

                    <vs-td :data="data[indextr].sexo">
                        {{data[indextr].sexo}}
                    </vs-td>

                    <vs-td :data="data[indextr].id">
                        <div class="flex">
                          <vs-button type="border" size="small" icon-pack="feather" @click="abrirEditar(data[indextr].id)" icon="icon-edit-2" color="success" class="mr-2"></vs-button>
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
import medio from '@/services/catalogos/sexo'
import formulario from'@/views/catalogo/Sexo/formulario.vue'
import editar from'@/views/catalogo/Sexo/editar.vue'

export default {
  components: {
    formulario,
    editar
  },
  data() {
    return {
      idE: 0,
      activeEditar:false,
      active:false,
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
    this.getMedio()
  },
  methods: {
    ocultarVentanaEditar(){
      this.activeEditar = false
      this.getMedio()
    },
    abrirEditar(id){
      this.idE = id
      this.activeEditar = true
    },
    eliminar(id){
      this.$vs.loading()
      medio.eliminar(id).then(response => {
          this.getMedio()
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
      this.getMedio()
    },
    abrirFormulario(){
      this. active = true
    },
     handleSearch(searching) {
      this.queryPage.nombre = searching
      this.getMedio()
    },
    pagina(){
      console.log('paginaaa', this.currentx)
    },
    getMedio() {
      console.log('medio')
      this.$vs.loading()
      // const vm = this
      medio.obtener(this.queryPage)
        .then(response => {
          console.log(response)
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
      this.getMedio()
    }
  }
}
</script>

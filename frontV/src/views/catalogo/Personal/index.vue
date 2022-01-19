<template>
  <div>
    <vx-card title="Agregar Personal" id="parentx-demo-5">
      <!-- search input -->
      <vs-button @click="abrirFormulario" color="primary" type="filled">Agregar nuevo registro</vs-button>
      <div class="custom-search d-flex justify-content-end">
        <b-form-group>
          <div class="d-flex align-items-center">
            <label class="mr-1">Buscar</label>
            <b-form-input
              v-model="searchTerm"
              placeholder="Buscar"
              type="text"
              @input="buscar"
            />
          </div>
        </b-form-group>
      </div> 

      <!-- table -->
      <vue-good-table
        styleClass="vgt-table"
        :columns="columns"
        :rows="medio"
        :rtl="true"
        
        
      >
        <template
          slot="table-row"
          slot-scope="props"
        >

          <!-- Column: Name -->
          <span
            v-if="props.column.field === 'fullName'"
            class="text-nowrap"
          >
            <b-avatar
              :src="props.row.avatar"
              class="mx-1"
            />
            <span class="text-nowrap">{{ props.row.nombre }}</span>
          </span>

          <!-- Column: Action -->
          <span v-else-if="props.column.field === 'action'">
            <span>
              <b-dropdown
                variant="link"
                toggle-class="text-decoration-none"
                no-caret
              >
                <template v-slot:button-content>
                  <feather-icon
                    icon="MoreVerticalIcon"
                    size="16"
                    class="text-body align-middle mr-25"
                  />
                </template>
                <b-dropdown-item 
                  @click="abrirEditar(props.row.id)">
                  <feather-icon
                    icon="Edit2Icon"
                    class="mr-50"
                  />
                  <span  >Edit</span>
                </b-dropdown-item>
                <b-dropdown-item>
                  <feather-icon
                    icon="TrashIcon"
                    class="mr-50"
                  />
                  <span>Delete</span>
                </b-dropdown-item>
              </b-dropdown>
            </span>
          </span>
          
        </template>

        <!-- pagination -->
        <template
          slot="pagination-bottom"
          slot-scope="props"
        >
          <div class="d-flex justify-content-between flex-wrap">
            
            <div>
              <b-pagination
                :value="totalPaginas"
                :total-rows="totalPaginas"
                :per-page="pageLength"
                first-number
                last-number
                align="right"
                prev-class="prev-item"
                next-class="next-item"
                class="mt-1 mb-0"
                @input="totalPaginas"
              >
                <template #prev-text>
                  <feather-icon
                    icon="ChevronLeftIcon"
                    size="18"
                  />
                </template>
                <template #next-text>
                  <feather-icon
                    icon="ChevronRightIcon"
                    size="18"
                  />
                </template>
              </b-pagination>
            </div>
          </div>
        </template>
      </vue-good-table>
      <b-pagination-nav
        :link-gen="linkGen"
        :number-of-pages="totalPaginas"
        use-router
        @input="cambiaP"
        class="mb-0"
      />
    </vx-card>
  </div>
</template>
<script>
import {
  BAvatar, BBadge, BPagination, BFormGroup, BFormInput, BFormSelect, BDropdown, BDropdownItem,
} from 'bootstrap-vue'
import servicio from '@/services/catalogos/persona'
import { VueGoodTable } from 'vue-good-table'
import 'vue-good-table/dist/vue-good-table.css'
import { BPaginationNav } from 'bootstrap-vue'

export default {
  components: {
    BPaginationNav,
    VueGoodTable,
    BAvatar,
    BBadge,
    BPagination,
    BFormGroup,
    BFormInput,
    BFormSelect,
    BDropdown,
    BDropdownItem,
  },
  data() {
    return {
      idE: 0,
      activeEditar:false,
      active:false,
      medio: '',
      currentx: 1,
      totalPaginas: 1,
      queryPage: {
        limit: 10,
        offset: 0,
        nombre: ''
      },
      dir: false,
      columns: [
        
        {
          label: 'Action',
          field: 'action',
        },
        {
          label: 'Apellido 1',
          field: 'apellido1',
        },
        {
          label: 'Apellido 2',
          field: 'apellido2',
        },
        {
          label: 'CURP',
          field: 'curp',
        },
        {
          label: 'CUIP',
          field: 'cuip',
        },
        
        {
          label: 'Numero de Empleado',
          field: 'numeroEmpleado',
        },
        {
          label: 'Id',
          field: 'id',
        },
        
      ],
      searchTerm: '',
    }
  },
  mounted() {
    this.getDatos()
  },
  methods: {
    cambiaP(pageNum) {
      console.log('cambiaaa', this.queryPage.offset = pageNum-1)
      this.queryPage.offset = (pageNum-1)*this.queryPage.limit 
      this.getDatos()
    },
    linkGen(pageNum) {
      return pageNum === 1 ? '?' : `?page=${pageNum}`
    },
    buscar(){
      console.log('buscar', this.searchTerm)
      this.queryPage.nombre = this.searchTerm
      this.getDatos()
    },
    ocultarVentanaEditar(){
      this.activeEditar = false
      this.getDatos()
    },
    abrirEditar(id){
      // console.log('aaaaa', this.idE)
      this.$router.push({ name: 'agregaPersonalEditar', params: {id:id} })

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
      this.$router.push({ name: 'agregaPersonal' })
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
  computed: {
  },
  watch: {
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
<style lang="scss">
</style>

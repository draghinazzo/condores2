export default [
  {
    path: '',
    component: () => import('@/layouts/main/Main.vue'),
    meta: {
        requiresAuth: true,
        rule: 'admin'
    },
    children: [

      {
        path: '/',
        redirect: '/dashboard',
      },

      {
        path: '/Catalogos',
        redirect: '/catalogos',
        name: 'Catalogos',
      },
      
      {
        path: '/dashboard',
        name: 'dashboard',
        component: () => import('@/views/pages/dashBoard.vue'),
        meta: {
          requiresAuth: true,  
          rule: 'admin',
        }
      },

      {
        path: '/catalogos/Medios',
        name: 'Medio',
        component: () => import('@/views/catalogo/Medio'),
        meta: {
            requiresAuth: true,
            rule: 'admin'
        }
      },
      {
        path: '/catalogos/Sexo',
        name: 'Sexo',
        component: () => import('@/views/catalogo/Sexo'),
        meta: {
            requiresAuth: true,
            rule: 'admin'
        }
      },
      {
        path: '/catalogos/TipoE',
        name: 'Tipo Empleado',
        component: () => import('@/views/catalogo/TipoE'),
        meta: {
            requiresAuth: true,
            rule: 'admin'
        }
      },
      {
        path: '/catalogos/Cargos',
        name: 'Cargo',
        component: () => import('@/views/catalogo/Cargo'),
        meta: {
            requiresAuth: true,
            rule: 'admin'
        }
      },
      {
        path: '/catalogos/Servicios',
        name: 'Servicio',
        component: () => import('@/views/catalogo/Servicio'),
        meta: {
            requiresAuth: true,
            rule: 'admin'
        }
      },
      
      {
        path: '/catalogos/Solicitante',
        name: 'Solicitante',
        component: () => import('@/views/catalogo/Solicitante'),
        meta: {
            requiresAuth: true,
            rule: 'admin'
        }
      },
      {
        path: '/misiones/Mantenimiento',
        name: 'Mantenimiento',
        component: () => import('@/views/misiones/Mantenimiento'),
        meta: {
            requiresAuth: true,
            rule: 'admin'
        }
      },
      {
        path: '/misiones/DireccionMision',
        name: 'Direccion de la mision',
        component: () => import('@/views/misiones/DireccionM'),
        meta: {
            requiresAuth: true,
            rule: 'admin'
        }
      },
      {
        path: '/misiones/Mision',
        name: 'Mision',
        component: () => import('@/views/misiones/Mision'),
        meta: {
            requiresAuth: true,
            rule: 'admin'
        }
      },
      {
        path: '/Helicopteros',
        name: 'Solicitante',
        component: () => import('@/views/helicopteros'),
        meta: {
            requiresAuth: true,
            rule: 'admin'
        }
      },
      
      {
        path: '/editarMision/:id',
        name: 'editarMision',
        component: () => import('@/views/misiones/Mision/editar.vue'),
        meta: {
          requiresAuth: true,  
          rule: 'admin',
        }
      },
      
      {
        path: '/guardarMision',
        name: 'guardarMision',
        component: () => import('@/views/misiones/Mision/formulario.vue'),
        meta: {
          requiresAuth: true,  
          rule: 'admin',
        }
      },

      {
        path: '/capacitacion/Cursos',
        name: 'cursos',
        component: () => import('@/views/capacitacion/Cursos'),
        meta: {
          requiresAuth: true,  
          rule: 'admin',
        }
      },

      {
        path: '/capacitacion/Instructor',
        name: 'Instructor',
        component: () => import('@/views/capacitacion/Instructor'),
        meta: {
          requiresAuth: true,  
          rule: 'admin',
        }
      },

      {
        path: '/capacitacion/Capacitacion',
        name: 'Capacitacion',
        component: () => import('@/views/capacitacion/Capacitacion'),
        meta: {
          requiresAuth: true,  
          rule: 'admin',
        }
      },

    ]

  },
]

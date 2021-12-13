export default [
  {
      icon: "HomeIcon",
      url: '/dashboard',
      name: "Inicio",
      slug: "dashboard",
  },
  {
    url: null,
    name: "Helicopteros",
    icon: "MenuIcon",
    submenu: [
      
      {
        url: '/Helicopteros',
        name: "Helicopteros",
        slug: "chat",
      },
    ],
  },
  {
    url: null,
    name: "Catalogos",
    icon: "MenuIcon",
    submenu: [
      
      {
        url: '/catalogos/Medios',
        name: "Medios",
        slug: "chat",
      },

      {
        url: '/catalogos/Sexo',
        name: "Sexo",
        slug: "chat",
      },
      
      {
        url: '/catalogos/TipoE',
        name: "Tipo Empleado",
        slug: "chat",
      },

      {
        url: '/catalogos/Cargos',
        name: "Cargos",
        slug: "chat",
      },

      { 
        url: '/catalogos/Servicios',
        name: "Servicios",
        slug: "chat",
      },
      
      { 
        url: '/catalogos/Solicitante',
        name: "Solicitante",
        slug: "chat",
      },
    ]
  },
  {
    url: null,
    name: "Misiones",
    icon: "MenuIcon",
    submenu:[
      {
        url: '/misiones/Mantenimiento',
        name: "Mantenimiento",
        slug: "chat",
      },
      {
        url: '/misiones/DireccionMision',
        name: "Direccion de la mision",
        slug: "chat",
      },
      {
        url: '/misiones/Mision',
        name: "Mision",
        slug: "chat",
      }
    ]
  },
  {
    url: null,
    name: "Capacitacion",
    icon: "MenuIcon",
    submenu:[
      {
        url: '/capacitacion/Cursos',
        name: "Cursos",
        slug: "chat",
      },
      {
        url: '/capacitacion/Instructor',
        name: "Instructor",
        slug: "chat",
      },
      {
        url: '/capacitacion/Capacitacion',
        name: "Capacitacion",
        slug: "chat",
      },
    ]
  }
]

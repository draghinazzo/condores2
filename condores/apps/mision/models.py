from django.db import models
from simple_history.models import HistoricalRecords
from apps.base.models import BaseModel



# Create your models here.
class catMedio(BaseModel):
    nombre = models.CharField(max_length=255)
    historical = HistoricalRecords()

    objects = models.Manager()
    
    @property
    def _history_user(self):
        return self.change_by

    @_history_user.setter
    def _history_user(self,value):
        self.chamge_by = value

    class Meta:
        verbose_name = 'Modelo Medio'
        verbose_name_plural = 'Modelo Medio'

    def __str__(self):
        return f'Medio {self.id}: {self.nombre}'

class catSolicitante(BaseModel):
    nombre = models.CharField(max_length=255)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.change_by

    @_history_user.setter
    def _history_user(self,value):
        self.chamge_by = value

    class Meta:
        verbose_name = 'Modelo CatSolicitante'
        verbose_name_plural = 'Modelo CatSolicitante'

    def __str__(self):
        return f'Solicitante {self.id}: {self.nombre}'

class catServicio(BaseModel):#TipoServicio
    nombre = models.CharField(max_length=255)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.change_by

    @_history_user.setter
    def _history_user(self,value):
        self.chamge_by = value

    class Meta:
        verbose_name = 'Modelo Servicio'
        verbose_name_plural = 'Modelo Servicio'

    def __str__(self):
        return f'Servicio {self.id}: {self.nombre}'

class catCargo(BaseModel):
    nombre = models.CharField(max_length=255)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.change_by

    @_history_user.setter
    def _history_user(self,value):
        self.chamge_by = value

    class Meta:
        verbose_name = 'Modelo Cargo'
        verbose_name_plural = 'Modelo Cargo'

    def __str__(self):
        return f'Cargo {self.id}: {self.nombre}'

class catSexo(BaseModel):
    sexo = models.CharField(max_length=255)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.change_by

    @_history_user.setter
    def _history_user(self,value):
        self.chamge_by = value

    class Meta:
        verbose_name = 'Modelo catalogo sexo'
        verbose_name_plural = 'Modelo catalogo sexo'

    def __str__(self):
        return f'Catalo de sexo {self.id}: {self.nombre}'      

class catTipoE(BaseModel):
    nombre = models.CharField(max_length=255)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.change_by

    @_history_user.setter
    def _history_user(self,value):
        self.chamge_by = value

    class Meta:
        verbose_name = 'Modelo tipo empleado'
        verbose_name_plural = 'Modelo tipo empleado'

    def __str__(self):
        return f'catalogo tipo empleado {self.id}: {self.nombre}'

class catInstitucion(BaseModel):
    nombre = models.CharField(max_length=255)

    @property
    def _history_user(self):
        return self.change_by

    @_history_user.setter
    def _history_user(self,value):
        self.chamge_by = value

    class Meta:
        verbose_name = 'Modelo catalogo instituciones'
        verbose_name_plural = 'Modelo catalogo instituciones'

    def __str__(self):
        return f'Catalo de instituciones {self.id}: {self.nombre}'  

class persona(BaseModel):
    esInstructor = models.BooleanField()
    capacidad = models.CharField(max_length=255)
    numeroEmpleado = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    apellido1 = models.CharField(max_length=255)
    apellido2 = models.CharField(max_length=255)
    curp = models.CharField(max_length=255)
    rfc = models.CharField(max_length=255)
    cuip = models.CharField(max_length=255)
    cuip = models.CharField(max_length=255)
    fechaNacimiento = models.DateField(null=True)
    grado = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    telefono_oficina = models.CharField(max_length=255)
    extension = models.CharField(max_length=255)
    telefono_celular = models.CharField(max_length=255)
    adscripcion_general = models.CharField(max_length=255)
    correo = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    tipo_empleado = models.ForeignKey(catTipoE, on_delete=models.SET_NULL, null=True)
    escolaridad = models.CharField(max_length=255)
    sexo = models.ForeignKey(catSexo, on_delete=models.SET_NULL, null=True)
    edad = models.CharField(max_length=255)
    antiguedad = models.CharField(max_length=255)
    
    numeroLicencia = models.CharField(max_length=255)
    vigencia = models.DateField(null=True)
    tipoLicencia = models.CharField(max_length=255)
    '''
    colonia = models.CharField(max_length=255)
    alcaldia = models.CharField(max_length=255)
    municipio = models.CharField(max_length=255)
    entidadFederativa = models.CharField(max_length=255)
    codigoPostal = models.CharField(max_length=255)
    '''
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.change_by

    @_history_user.setter
    def _history_user(self,value):
        self.chamge_by = value

    class Meta:
        verbose_name = 'Modelo tipo persona'
        verbose_name_plural = 'Modelo tipo persona'

    def __str__(self):
        return f'persona {self.id}: {self.nombre}'

class instructores(BaseModel):
    persona = models.ForeignKey(persona, on_delete=models.SET_NULL, null=True)
    activo = models.BooleanField(default=True)
    historical = HistoricalRecords()


    @property
    def _history_user(self):
        return self.change_by

    @_history_user.setter
    def _history_user(self,value):
        self.chamge_by = value

    class Meta:
        verbose_name = 'Modelo tipo instructores'
        verbose_name_plural = 'Modelo tipo instructores'

    def __str__(self):
        return f'instructores {self.id}: {self.activo}'  

class descripcion_emergencia(BaseModel):
    descripcionEmergencia = models.JSONField()
    historical = HistoricalRecords()


    @property
    def _history_user(self):
        return self.change_by

    @_history_user.setter
    def _history_user(self,value):
        self.chamge_by = value

    class Meta:
        verbose_name = 'Modelo tipo descripcion de emergencia'
        verbose_name_plural = 'Modelo tipo descripcion de emergencia'

    def __str__(self):
        return f'instructores {self.id}: {self.descripcionEmergencia}'

class solicitud_emergencia(BaseModel):
    fechaHora = models.DateTimeField()
    medio = models.ForeignKey(catMedio, on_delete=models.SET_NULL, null=True)
    institucion = models.ForeignKey(catInstitucion, on_delete=models.SET_NULL, null=True)
    nombreSolicitante = models.CharField(max_length=255)
    cargo = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    servicio = models.ForeignKey(catServicio, on_delete=models.SET_NULL, null=True)
    

    historical = HistoricalRecords()


    @property
    def _history_user(self):
        return self.change_by

    @_history_user.setter
    def _history_user(self,value):
        self.chamge_by = value

    class Meta:
        verbose_name = 'Modelo tipo solicitud de emergencia'
        verbose_name_plural = 'Modelo tipo solicitud de emergencia'

    def __str__(self):
        return f'instructores {self.id}: {self.nombreSolicitante}'

class puente_emergencia(BaseModel):
    solicitud = models.ForeignKey(solicitud_emergencia, on_delete=models.SET_NULL, null=True)
    servicio = models.ForeignKey(catServicio, on_delete=models.SET_NULL, null=True)
    emergencia = models.ForeignKey(descripcion_emergencia, on_delete=models.SET_NULL, null=True)
    status = models.BooleanField(default=True)
    

    historical = HistoricalRecords()


    @property
    def _history_user(self):
        return self.change_by

    @_history_user.setter
    def _history_user(self,value):
        self.chamge_by = value

    class Meta:
        verbose_name = 'Modelo tipo solicitud de emergencia'
        verbose_name_plural = 'Modelo tipo solicitud de emergencia'

    def __str__(self):
        return f'instructores {self.id}: {self.nombreSolicitante}'        

"""
class solicitante(BaseModel):
    nombre = models.CharField(max_length=255)
    apellido1 = models.CharField(max_length=255)
    apellido2 = models.CharField(max_length=255)
    cargo = models.ForeignKey(catCargo, on_delete=models.SET_NULL, null=True)
    telefonoContacto = models.CharField(max_length=255)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.change_by

    @_history_user.setter
    def _history_user(self,value):
        self.chamge_by = value

    class Meta:
        verbose_name = 'Modelo Nombre Solicitante'
        verbose_name_plural = 'Modelo Nombre Solicitante'

    def __str__(self):
        return f'Solicitante {self.id}: {self.nombre} {self.apellido1} {self.apellido2}'

class Helicopteros(BaseModel):
    placa = models.CharField(max_length=255)
    modelo = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    marca = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.change_by

    @_history_user.setter
    def _history_user(self,value):
        self.chamge_by = value

    class Meta:
        verbose_name = 'Modelo Helicoptero'
        verbose_name_plural = 'Modelo Helicoptero'

    def __str__(self):
        return f'Helicopteros {self.id}: {self.placa} {self.modelo} {self.year}'

class direccionMision(BaseModel):
    calle = models.CharField(max_length=255)
    colonia = models.CharField(max_length=255)
    alcaldia = models.CharField(max_length=255)
    entidadFederativa = models.CharField(max_length=255)
    coordenadas = models.CharField(max_length=255)
    poblacionCercana = models.CharField(max_length=255)
    referencia = models.CharField(max_length=255)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.change_by

    @_history_user.setter
    def _history_user(self,value):
        self.chamge_by = value

    class Meta:
        verbose_name = 'Modelo Direccion Mision'
        verbose_name_plural = 'Modelo Direccion Mision'

    def __str__(self):
        return f'DireccionMision {self.id}: {self.calle} {self.colonia} {self.alcaldia}'

class mision(BaseModel):
    medio = models.ForeignKey(catMedio, on_delete=models.SET_NULL, null=True)
    solicitante = models.ForeignKey(catSolicitante, on_delete=models.SET_NULL, null=True)
    servicio = models.ForeignKey(catServicio, on_delete=models.SET_NULL, null=True)
    ubicacion = models.ForeignKey(direccionMision, on_delete=models.SET_NULL, null=True)
    helicoptero = models.ForeignKey(Helicopteros, on_delete=models.SET_NULL, null=True)
    nombre = models.CharField(max_length=255)
    apellido1 = models.CharField(max_length=255)
    apellido2 = models.CharField(max_length=255)
    numeroEmpleado = models.CharField(max_length=255)
    historical = HistoricalRecords()
    fechaNacimiento = models.DateField(null=True)
    rfc = models.CharField(max_length=255, null=True)
    curp = models.CharField(max_length=255, null=True)
    sexo = models.ForeignKey(catSexo, on_delete=models.SET_NULL, null=True)
    fechaAlta = models.DateField(null=True)
    cuip = models.CharField(max_length=255, null=True)
    tipoEmpleado = models.ForeignKey(catTipoE, on_delete=models.SET_NULL, null=True)

    @property
    def _history_user(self):
        return self.change_by

    @_history_user.setter
    def _history_user(self,value):
        self.chamge_by = value

    class Meta:
        verbose_name = 'Modelo Mision'
        verbose_name_plural = 'Modelo Mision'

    def __str__(self):
        return f'mision {self.id}: {self.medio} {self.solicitante} {self.servicio}'

class bitacora(BaseModel):
    mision = models.ForeignKey(mision, on_delete=models.SET_NULL, null=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.change_by

    @_history_user.setter
    def _history_user(self,value):
        self.chamge_by = value

    class Meta:
        verbose_name = 'Modelo Bitacora'
        verbose_name_plural = 'Modelo Bitacora'

    def __str__(self):
        return f'bitacora {self.id}: {self.mision}'

class tripulacion(BaseModel):
    mision = models.ForeignKey(mision, on_delete=models.SET_NULL, null=True)
    nombre = models.CharField(max_length=255)
    apellido1 = models.CharField(max_length=255)
    apellido2 = models.CharField(max_length=255)
    numeroEmpleado = models.CharField(max_length=255)
    historical = HistoricalRecords()
    fechaNacimiento = models.DateField(null=True)
    rfc = models.CharField(max_length=255,null=True)
    curp = models.CharField(max_length=255, null=True)
    sexo = models.ForeignKey(catSexo, on_delete=models.SET_NULL, null=True)
    fechaAlta = models.DateField(null=True)
    cuip = models.CharField(max_length=255, null=True)
    tipoEmpleado = models.ForeignKey(catTipoE, on_delete=models.SET_NULL, null=True)


    @property
    def _history_user(self):
        return self.change_by

    @_history_user.setter
    def _history_user(self,value):
        self.chamge_by = value

    class Meta:
        verbose_name = 'Modelo Tripulacion'
        verbose_name_plural = 'Modelo Tripulacion'

    def __str__(self):
        return f'Tripulacion {self.id}: {self.mision} {self.numeroEmpleado} {self.nombre}'

class mantenimiento(BaseModel):
    fechaInicio = models.DateField()
    helicoptero = models.ForeignKey(Helicopteros, on_delete=models.SET_NULL, null=True)
    nombre = models.CharField(max_length=255)
    apellido1 = models.CharField(max_length=255)
    apellido2 = models.CharField(max_length=255)
    numeroEmpleado = models.CharField(max_length=255)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.change_by

    @_history_user.setter
    def _history_user(self,value):
        self.chamge_by = value

    class Meta:
        verbose_name = 'Modelo Mantenimineto'
        verbose_name_plural = 'Modelo Mantenimiento'

    def __str__(self):
        return f'mantenimiento {self.id}: {self.fechaInicio} mecanico: {self.nombre}'
"""
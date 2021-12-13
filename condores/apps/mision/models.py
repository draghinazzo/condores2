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

class catServicio(BaseModel):
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
        return f'Catalo de sexo {self.id}: {self.nombre}'

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
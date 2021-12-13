from django.db import models
from simple_history.models import HistoricalRecords
from apps.base.models import BaseModel

# Create your models here.
class instructor(BaseModel):
    nombre = models.CharField(max_length=255)
    apellido1 = models.CharField(max_length=255)
    apellido2 = models.CharField(max_length=255)
    especialidad = models.CharField(max_length=255)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.change_by

    @_history_user.setter
    def _history_user(self,value):
        self.chamge_by = value

    class Meta:
        verbose_name = 'Modelo Instructor'
        verbose_name_plural = 'Modelo Instructor'

    def __str__(self):
        return f'Instructor {self.id}: {self.especialidad} instructor: {self.nombre}'

class cursos(BaseModel):
    nombreCurso = models.CharField(max_length=255)
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    instructor = models.ForeignKey(instructor, on_delete=models.SET_NULL, null=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.change_by

    @_history_user.setter
    def _history_user(self,value):
        self.chamge_by = value

    class Meta:
        verbose_name = 'Modelo Cursos'
        verbose_name_plural = 'Modelo Cursos'

    def __str__(self):
        return f'curso {self.id}: {self.nombreCurso} Fecha Inicio: {self.fechaInicio}'

class capacitacion(BaseModel):
    numeroEmpleado = models.CharField(max_length=255)
    curso = models.ForeignKey(cursos, on_delete=models.SET_NULL, null=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.change_by

    @_history_user.setter
    def _history_user(self,value):
        self.chamge_by = value

    class Meta:
        verbose_name = 'Modelo capacitacion'
        verbose_name_plural = 'Modelo capacitacion'

    def __str__(self):
        return f'capacitacion {self.id}: {self.numeroEmpleado} numeroEmpleado: {self.numeroEmpleado}'
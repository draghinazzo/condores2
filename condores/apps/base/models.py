from django.db import models
from simple_history.models import HistoricalRecords
# Create your models here.

class BaseModel(models.Model):
    id = models.AutoField(primary_key = True)
    state = models.BooleanField('Estado', default = True)
    created_date = models.DateField('Fecha de Creacion', auto_now = False, auto_now_add = False, null=True, blank=True)
    modified_date = models.DateField('Fecha de Modificacion', auto_now = True, auto_now_add = False)
    deletec_date = models.DateField('Fecha de Eliminacion', auto_now = True, auto_now_add = False)

    class Meta:
        abstract = True
        verbose_name = 'Modelos Base'
        verbose_name_plural = 'Modelos Base'
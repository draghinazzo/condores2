from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from simple_history.models import HistoricalRecords
from apps.base.models import BaseModel


class permisos(BaseModel):
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
        verbose_name = 'Modelo permiso'
        verbose_name_plural = 'Modelo permisos'

    def __str__(self):
        return f'Permisos {self.id}: {self.nombre}'

class UserManager(BaseUserManager):
    def _create_user(self, username, email, name,last_name, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username = username,
            email = email,
            name = name,
            last_name = last_name,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email, name,last_name, password=None, **extra_fields):
        return self._create_user(username, email, name,last_name, password, False, False, **extra_fields)

    def create_superuser(self, username, email, name,last_name, password=None, **extra_fields):
        return self._create_user(username, email, name,last_name, password, True, True, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    permissions = models.ForeignKey(permisos, on_delete=models.SET_NULL, null=True)
    username = models.CharField(max_length = 255, unique = True)
    email = models.EmailField('Correo Electrónico',max_length = 255, unique = True,)
    name = models.CharField('Nombres', max_length = 255, blank = True, null = True)
    last_name = models.CharField('Apellidos', max_length = 255, blank = True, null = True)
    image = models.ImageField('Imagen de perfil', upload_to='perfil/', max_length=255, null=True, blank = True)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    historical = HistoricalRecords()
    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','name','last_name']

    def __str__(self):
        return f'{self.name} {self.last_name}'
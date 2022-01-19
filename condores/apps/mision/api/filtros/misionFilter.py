import django_filters
from apps.mision.models import persona

class personaFilters(django_filters.FilterSet):
    id = django_filters.NumberFilter()
    numeroEmpleado = django_filters.CharFilter(field_name='numeroEmpleado', lookup_expr='icontains')

    class Meta:
        model = persona
        fields = ['id', 'numeroEmpleado', 'nombre', 'esInstructor', 'capacidad', 'apellido1', 'apellido2', 'curp', 'rfc', 'fechaNacimiento', 'grado', 'telefono', 'telefono_oficina', 'extension', 'telefono_celular']

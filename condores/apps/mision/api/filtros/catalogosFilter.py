import django_filters
from apps.mision.models import catMedio, catCargo, catServicio, catSolicitante, catSexo, catTipoE

class catMedioFilters(django_filters.FilterSet):
    id = django_filters.NumberFilter()
    nombre = django_filters.CharFilter(field_name='nombre', lookup_expr='icontains')

    class Meta:
        model = catMedio
        fields = ['id', 'nombre']

class catCargoFilters(django_filters.FilterSet):
    id = django_filters.NumberFilter()
    nombre = django_filters.CharFilter(field_name='nombre', lookup_expr='icontains')

    class Meta:
        model = catCargo
        fields = ['id', 'nombre']

class catCServicioFilters(django_filters.FilterSet):
    id = django_filters.NumberFilter()
    nombre = django_filters.CharFilter(field_name='nombre', lookup_expr='icontains')

    class Meta:
        model = catServicio
        fields = ['id', 'nombre']

class catSexoFilters(django_filters.FilterSet):
    id = django_filters.NumberFilter()
    nombre = django_filters.CharFilter(field_name='sexo', lookup_expr='icontains')

    class Meta:
        model = catSexo
        fields = ['id', 'sexo']

class catTipoeFilters(django_filters.FilterSet):
    id = django_filters.NumberFilter()
    nombre = django_filters.CharFilter(field_name='nombre', lookup_expr='icontains')

    class Meta:
        model = catTipoE
        fields = ['id', 'nombre']

class catCSolicitanteFilters(django_filters.FilterSet):
    id = django_filters.NumberFilter()
    nombre = django_filters.CharFilter(field_name='nombre', lookup_expr='icontains')

    class Meta:
        model = catSolicitante
        fields = ['id', 'nombre']

from django.urls import path
from apps.mision.api.views.general_views import medioListAPIView
from apps.mision.api.views.mision_views import misionListCreateAPIView, misionRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('medios/', medioListAPIView.as_view(), name = 'Medio' ),
    path('misiones/mision', misionListCreateAPIView.as_view(), name = 'misiones_create' ),
    path('misiones/retrieve/<int:pk>/', misionRetrieveUpdateDestroyAPIView.as_view(), name = 'misiones_retrieve' ),
]
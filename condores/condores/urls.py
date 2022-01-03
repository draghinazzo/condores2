from apps.mision.api.views.mision_views import CustomTokenRefreshView, CustomTokenView
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from apps.users.api.api import user_api_view, user_details_api_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView, TokenVerifyView
from apps.apiConsulta.placaConsulta import placaConsulta, imagenConsulta

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuario/', user_api_view, name = 'usuario_api'),
    path('usuario/<int:pk>/', user_details_api_view, name = 'usuario_detail_api_view'),
    path('api/misiones/', include('apps.mision.api.routers')),
    path('api/capacitacion/', include('apps.capacitacion.api.routers')),
    #path('auth/', include('apps.users.api.url')),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh', TokenRefreshView.as_view()),
    path ('api/token/verify', TokenVerifyView.as_view ()),
    path('api/token/refresh2', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('api/tokenC', CustomTokenView.as_view()),
    path('api/Consulta/<int:placa>', placaConsulta.consulta, name='consulta'),
    path('api/consultaImagen/<int:placa>', imagenConsulta.consulta, name='consultaImagen'),

]

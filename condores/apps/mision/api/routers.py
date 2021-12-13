from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from apps.mision.api.views.mision_views import misionViewSet, catMedioViewSet, catSolicitanteViewSet, catServicioViewSet, catCargoViewSet,solicitanteViewSet,HelicopterosViewSet, direccionMisionViewSet, bitacoraViewSet, tripulacionViewSet,mantenimientoViewSet, HelicopterosSelectViewSet, catSexoViewSet, catTipoeViewSet, direccionMSelectisionViewSet, medioSelectViewSet, servicioSelectViewSet, solicitanteSelectViewSet,sexoSelectViewSet,tipoESelectViewSet


router = DefaultRouter()

router.register(r'misiones', misionViewSet)
router.register(r'medioSelect', medioSelectViewSet)
router.register(r'servicioSelect', servicioSelectViewSet)
router.register(r'medio', catMedioViewSet)
router.register(r'sexo', catSexoViewSet)
router.register(r'sexoSelect', sexoSelectViewSet)
router.register(r'tipoE', catTipoeViewSet)
router.register(r'tipoESelect', tipoESelectViewSet)
router.register(r'solicitante', catSolicitanteViewSet)
router.register(r'solicitanteSelect', solicitanteSelectViewSet)
router.register(r'servicio', catServicioViewSet)
router.register(r'cargo', catCargoViewSet)
router.register(r'solicitante', solicitanteViewSet)
router.register(r'helicoptero', HelicopterosViewSet)
router.register(r'helicopteroSelect', HelicopterosSelectViewSet)
router.register(r'direccionM', direccionMisionViewSet)
router.register(r'direccionMSelect', direccionMSelectisionViewSet)
router.register(r'bitacora', bitacoraViewSet)
router.register(r'tripulacion', tripulacionViewSet)
router.register(r'mantenimiento', mantenimientoViewSet)

urlpatterns = router.urls
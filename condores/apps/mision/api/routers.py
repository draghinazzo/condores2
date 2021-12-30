from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from apps.mision.api.views.mision_views import catMedioViewSet, catSolicitanteViewSet, catServicioViewSet, catCargoViewSet, catSexoViewSet, catTipoeViewSet, medioSelectViewSet, servicioSelectViewSet, solicitanteSelectViewSet,sexoSelectViewSet,tipoESelectViewSet, catInstitucionViewSet, personaViewSet,licenciaPersonaViewSet, domiciolioPersonaViewSet,  intructoresViewSet, descripcionEmergenciaViewSet, solicitudEmergenciaViewSet, institucionctViewSet
"""
misionViewSet, HelicopterosViewSet, direccionMisionViewSet, bitacoraViewSet, tripulacionViewSet,mantenimientoViewSet, direccionMSelectisionViewSet, HelicopterosSelectViewSet, solicitanteViewSet
"""


router = DefaultRouter()

#router.register(r'misiones', misionViewSet)
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

router.register(r'selectInstitucion', institucionctViewSet)#<-
router.register(r'catInstitucion', catInstitucionViewSet)#<-
router.register(r'persona', personaViewSet)#<-
router.register(r'licenciaPersona', licenciaPersonaViewSet)#<-
router.register(r'domiciolioPersona', domiciolioPersonaViewSet)#<-
router.register(r'intructores', intructoresViewSet)
router.register(r'descripcionEmergencia', descripcionEmergenciaViewSet)
router.register(r'solicitudEmergencia', solicitudEmergenciaViewSet)
"""
router.register(r'solicitante', solicitanteViewSet)
router.register(r'helicoptero', HelicopterosViewSet)
router.register(r'helicopteroSelect', HelicopterosSelectViewSet)
router.register(r'direccionM', direccionMisionViewSet)
router.register(r'direccionMSelect', direccionMSelectisionViewSet)
router.register(r'bitacora', bitacoraViewSet)
router.register(r'tripulacion', tripulacionViewSet)
router.register(r'mantenimiento', mantenimientoViewSet)
"""
urlpatterns = router.urls
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from apps.capacitacion.api.views.capacitacion_views import instructorViewSet, cursoViewSet, instructorSelectViewSet, capacitacionViewSet, cursoSelectViewSet


router = DefaultRouter()

router.register(r'instructor', instructorViewSet)
router.register(r'curso', cursoViewSet)
router.register(r'cursoSelect', cursoSelectViewSet)
router.register(r'instructorSelect', instructorSelectViewSet)
router.register(r'capacitacion', capacitacionViewSet)

urlpatterns = router.urls
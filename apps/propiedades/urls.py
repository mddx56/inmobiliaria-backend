from django.urls import include, path
from rest_framework import routers
from apps.propiedades import views

router = routers.DefaultRouter()
router.register("tipoinmuebles", views.TipoInmuebleView)
router.register("caracteristicas", views.CaracteristicaView)
router.register("inmuebles", views.InmuebleView)
router.register("terrenos", views.TerrenoView)
router.register("departamentos", views.DepartamentoView)
router.register("casas", views.CasaView)
router.register("imagenes", views.ImagenView)
router.register("areas", views.AreaView)
router.register("puntos", views.PuntoView)
router.register("ciudads", views.CiudadView)
router.register("zonas", views.ZonaView)


urlpatterns = [
    path("estate/", include(router.urls)),
]

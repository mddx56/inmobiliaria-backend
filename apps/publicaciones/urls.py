from django.urls import include, path
from rest_framework import routers
from apps.publicaciones import views

router = routers.DefaultRouter()
router.register("tipoofertas", views.TipoOfertaView)
router.register("anuncios", views.AnuncioView)


urlpatterns = [
    path("post/", include(router.urls)),
]

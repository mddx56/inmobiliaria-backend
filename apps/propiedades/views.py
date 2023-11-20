from rest_framework import viewsets
from apps.propiedades.models import (
    Caracteristica,
    Inmueble,
    TipoInmueble,
    Area,
    Casa,
    Ciudad,
    Departamento,
    Imagen,
    Punto,
    Terreno,
    Zona,
)

from apps.propiedades.serializers import (
    CaracteristicaSerializer,
    InmuebleSerializer,
    TipoInmuebleSerializer,
    AreaSerializer,
    CiudadSerializer,
    CasaSerializer,
    DepartamentoSerializer,
    PuntoSerializer,
    ImagenSerializer,
    TerrenoSerializer,
    ZonaSerializer,
)


class TipoInmuebleView(viewsets.ModelViewSet):
    serializer_class = TipoInmuebleSerializer
    queryset = TipoInmueble.objects.all()


class CaracteristicaView(viewsets.ModelViewSet):
    serializer_class = CaracteristicaSerializer
    queryset = Caracteristica.objects.all()


class InmuebleView(viewsets.ModelViewSet):
    serializer_class = InmuebleSerializer
    queryset = Inmueble.objects.all()


class DepartamentoView(viewsets.ModelViewSet):
    serializer_class = DepartamentoSerializer
    queryset = Departamento.objects.all()


class TerrenoView(viewsets.ModelViewSet):
    serializer_class = TerrenoSerializer
    queryset = Terreno.objects.all()


class CasaView(viewsets.ModelViewSet):
    serializer_class = CasaSerializer
    queryset = Casa.objects.all()


class ImagenView(viewsets.ModelViewSet):
    serializer_class = ImagenSerializer
    queryset = Imagen.objects.all()


class AreaView(viewsets.ModelViewSet):
    serializer_class = AreaSerializer
    queryset = Area.objects.all()


class PuntoView(viewsets.ModelViewSet):
    serializer_class = PuntoSerializer
    queryset = Punto.objects.all()


class CiudadView(viewsets.ModelViewSet):
    serializer_class = CiudadSerializer
    queryset = Ciudad.objects.all()


class ZonaView(viewsets.ModelViewSet):
    serializer_class = ZonaSerializer
    queryset = Zona.objects.all()


class TipoInmuebleView(viewsets.ModelViewSet):
    serializer_class = TipoInmuebleSerializer
    queryset = TipoInmueble.objects.all()

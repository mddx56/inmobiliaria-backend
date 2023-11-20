from rest_framework import serializers

from .models import (
    TipoInmueble,
    Area,
    Caracteristica,
    Inmueble,
    Casa,
    Ciudad,
    Departamento,
    Imagen,
    Punto,
    Terreno,
    Zona,
)


class TipoInmuebleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoInmueble
        fields = "__all__"


class CaracteristicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caracteristica
        fields = "__all__"


class InmuebleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inmueble
        fields = "__all__"


class TerrenoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Terreno
        fields = "__all__"


class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = "__all__"


class CasaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Casa
        fields = "__all__"


class ImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagen
        fields = "__all__"


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = "__all__"


class PuntoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Punto
        fields = "__all__"


class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = "__all__"


class ZonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zona
        fields = "__all__"

from rest_framework import serializers
from .models import TipoOferta, Anuncio


class TipoOfertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoOferta
        fields = "__all__"


class AnuncioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anuncio
        fields = "__all__"

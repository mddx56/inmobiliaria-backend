from rest_framework import viewsets

from .models import TipoOferta, Anuncio

from .serializers import TipoOfertaSerializer, AnuncioSerializer


class TipoOfertaView(viewsets.ModelViewSet):
    serializer_class = TipoOfertaSerializer
    queryset = TipoOferta.objects.all()


class AnuncioView(viewsets.ModelViewSet):
    serializer_class = AnuncioSerializer
    queryset = Anuncio.objects.all()

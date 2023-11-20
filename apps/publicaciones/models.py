import uuid
from django.db import models
from apps.propiedades.models import Inmueble, Zona


class TipoOferta(models.Model):
    class Meta:
        verbose_name = "TipoOferta"
        verbose_name_plural = "TipoOferas"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=250, null=False)
    descripcion = models.TextField(max_length=2400, blank=True, null=True)


class Anuncio(models.Model):
    class Meta:
        verbose_name = "Anuncio"
        verbose_name_plural = "Anuncios"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titulo = models.CharField(max_length=255, blank=True, null=True)
    etiqueta = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.TextField(max_length=2400, blank=True, null=True)
    seoUrl = models.URLField(max_length=350)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    tipo_oferta = models.ForeignKey(TipoOferta, on_delete=models.CASCADE)
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE)
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE)

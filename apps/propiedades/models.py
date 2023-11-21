import uuid
from django.db import models
from django.utils import timezone


class TipoInmueble(models.Model):
    class Meta:
        verbose_name = "TipoInmueble"
        verbose_name_plural = "TipoInmuebles"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=255, unique=True)
    titulo = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.TextField(max_length=2400, blank=True, null=True)

    def __str__(self) -> str:
        return f"Nombre : {self.nombre}"


class Caracteristica(models.Model):
    class Meta:
        verbose_name = "Caracteristica"
        verbose_name_plural = "Caracteristicas"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=250, null=False)
    tipo_inmueble = models.ForeignKey(
        TipoInmueble, related_name="tipo_inmueble_character", on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f"Nombre : {self.nombre}, {self.tipo_inmueble.nombre}"


class Ciudad(models.Model):
    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=250, null=False)
    departamento = models.CharField(max_length=250, null=False)

    def __str__(self) -> str:
        return f"Nombre : {self.nombre}"


class Zona(models.Model):
    class Meta:
        verbose_name = "Zona"
        verbose_name_plural = "Zonas"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=250, null=False)
    descripcion = models.TextField(max_length=2400, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    # area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name="area_zona")
    ciudad = models.ForeignKey(
        Ciudad, on_delete=models.CASCADE, related_name="ciudad_zona", null=True
    )

    def __str__(self) -> str:
        return f"Nombre : {self.nombre}"


class Inmueble(models.Model):
    class Meta:
        verbose_name = "Inmueble"
        verbose_name_plural = "Inmuebles"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    codigo = models.CharField(max_length=255, blank=True, null=True)
    oferta = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    gastos_comunes = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True, default=0
    )
    disposicion = models.CharField(blank=True, default="")
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    caracteristica = models.ManyToManyField(Caracteristica)
    tipo_inmueble = models.ForeignKey(
        TipoInmueble, on_delete=models.CASCADE, related_name="tipo_inmueble"
    )
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f"Direccion : {self.direccion}, Tipo {self.tipo_inmueble.nombre} - {self.zona.nombre}"


class Terreno(Inmueble):
    superficie = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f"Terreno : {self.id}"


class Departamento(Inmueble):
    superficie_construida = models.DecimalField(max_digits=10, decimal_places=2)
    superficie = models.DecimalField(max_digits=10, decimal_places=2)
    anio_construccion = models.PositiveIntegerField(blank=True, default=0)
    dormitorios = models.PositiveIntegerField(blank=True, default=0)
    banios = models.PositiveIntegerField(blank=True, default=0)
    parqueos = models.PositiveIntegerField(blank=True, default=0)
    piso = models.PositiveIntegerField(blank=True, default=0)
    cantidad_pisos = models.PositiveIntegerField(blank=True, default=0)

    def __str__(self) -> str:
        return f"Departamento : {self.id}"


class Casa(Inmueble):
    superficie_construida = models.DecimalField(max_digits=10, decimal_places=2)
    superficie_inmmuebele = models.DecimalField(max_digits=10, decimal_places=2)
    anio_construccion = models.PositiveIntegerField(blank=True, default=0)
    dormitorios = models.PositiveIntegerField(blank=True, default=0)
    banios = models.PositiveIntegerField(blank=True, default=0)
    parqueos = models.PositiveIntegerField(blank=True, default=0)
    plantas = models.PositiveIntegerField(blank=True, default=0)

    def __str__(self) -> str:
        return f"Casa : {self.id}"


class Imagen(models.Model):
    class Meta:
        verbose_name = "Imagen"
        verbose_name_plural = "Imagenes"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.URLField(max_length=350)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    inmueble = models.ForeignKey(
        Inmueble, related_name="imagen_inmueble", on_delete=models.CASCADE
    )


class Area(models.Model):
    class Meta:
        verbose_name = "Area"
        verbose_name_plural = "Areas"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    dimencion = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, default=0
    )
    isRadio = models.BooleanField(default=True, blank=False)
    inmueble = models.ForeignKey(
        Inmueble, related_name="Ubicacion", on_delete=models.CASCADE
    )


class Punto(models.Model):
    class Meta:
        verbose_name = "Punto"
        verbose_name_plural = "Puntos"

    latitud = models.DecimalField(max_digits=9, decimal_places=6)
    longitud = models.DecimalField(max_digits=9, decimal_places=6)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name="area_puntos")

    # nAmbientes = models.PositiveIntegerField(default=0, blank=True)
    # nParqueos = models.PositiveIntegerField(default=0, blank=True)
    # nGarajes = models.PositiveIntegerField(default=0, blank=True)

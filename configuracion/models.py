from django.db import models
from ckeditor.fields import RichTextField
ORDEN_CHOICES = (
    ('1', '1',),
    ('2', '2',),
    ('3', '3',),
    ('4', '4',),
)
SLIDER_CHOICES = (
    ('PRINCIPAL', 'PRINCIPAL',),
    ('SECUNDARIO', 'SECUNDARIO',),
)
FORMATO_CHOICES = (
    ('1', '1',),
    ('2', '2',),
)
class Menu(models.Model):
    titulo = models.TextField(
        null=True, blank=True,
        verbose_name="Titulo",
        help_text="Titulo",
    )
    descripcion = models.TextField(
        null=True, blank=True,
        verbose_name="Descripción",
        help_text="Descripción",
    )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class SubMenu(models.Model):
    titulo = models.TextField(
        null=True, blank=True,
        verbose_name="Titulo",
        help_text="Titulo",
    )
    descripcion = models.TextField(
        null=True, blank=True,
        verbose_name="Descripción",
        help_text="Descripción",
    )
    menu = models.ForeignKey(
        Menu, on_delete=models.DO_NOTHING,
        verbose_name="Menu",
        help_text="Menu",
        blank=True, null=True
    )
    url = models.TextField(
        verbose_name='URL Document',
        blank=True, null=True
    )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Noticia(models.Model):
    titulo = models.TextField(
        null=True, blank=True,
        verbose_name="Titulo",
        help_text="Titulo",
    )
    slug = models.CharField(
        null=True, blank=True,
        verbose_name="Slug",
        help_text="Slug", max_length=100
    )
    descripcion = RichTextField()
    age = models.CharField(
        null=True, blank=True, max_length=100,
        verbose_name="Año",
        help_text="Año",
    )
    campo1 = models.CharField(
        null=True, blank=True, max_length=300,
        verbose_name="campo1",
        help_text="campo1",
    )
    campo2 = models.CharField(
        null=True, blank=True, max_length=300,
        verbose_name="campo2",
        help_text="campo2",
    )

    month = models.CharField(
        null=True, blank=True, max_length=300,
        verbose_name="redirigir",
        help_text="redirigir",
    )
    orden = models.CharField(max_length=30, choices=ORDEN_CHOICES,
                             verbose_name='Estado:',
                             null=True,
                             blank=True)
    imagen = models.ImageField(
        null=False, blank=False,
        verbose_name="Imagen ",
        help_text="Imagen ",
    )
    description = models.TextField(
        null=True, blank=True,
        verbose_name="Descripcion",
        help_text="Descripcion",
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["id"]
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"

    def __str__(self):
        return self.titulo

class Pagina(models.Model):
    titulo = models.TextField(
        null=True, blank=True,
        verbose_name="Titulo",
        help_text="Titulo",
    )
    slug = models.CharField(
        null=True, blank=True,
        verbose_name="Slug",
        help_text="Slug", max_length=100
    )
    imagen = models.ImageField(
        null=False, blank=False,
        verbose_name="Imagen ",
        help_text="Imagen ",
    )
    formato = models.CharField(max_length=30, choices=FORMATO_CHOICES,
                              verbose_name='Estado:',
                              null=True,
                              blank=True)
    descripcion = RichTextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Slider(models.Model):
    name = models.CharField(
        null=False, blank=False, max_length=50,
        verbose_name="Nombre ",
        help_text="Nombre ",
    )
    imagen = models.ImageField(
        null=False, blank=False,
        verbose_name="Imagen ",
        help_text="Imagen ",
    )
    descripcion = models.TextField(
        null=True, blank=True,
        verbose_name="Descripción",
        help_text="Descripción",
    )
    tipo = models.CharField(max_length=30, choices=SLIDER_CHOICES,
                               verbose_name='Estado:',
                               null=True,
                               blank=True)
    orden = models.CharField(max_length=30, choices=ORDEN_CHOICES,
                            verbose_name='Estado:',
                            null=True,
                            blank=True)
    url = models.TextField(
        verbose_name='URL Document',

        blank=True, null=True
    )


    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["id"]
        verbose_name = "Slider",
        verbose_name_plural = "Slider"

    def __str__(self):
        return self.name

class Document(models.Model):
    titulo = models.CharField(
        null=False, blank=False, max_length=100,
        verbose_name="Nombre ",
        help_text="Nombre ",
    )
    description = models.TextField(
        null=True, blank=True,
        verbose_name="Descripcion",
        help_text="Descripcion",
    )
    url = models.TextField(
        verbose_name='URL Document',

        blank=True, null=True
    )
    archivo = models.FileField(
        verbose_name='URL Document',
        upload_to='upload/documento',
        blank=True, null=True
    )
    pagina = models.ForeignKey(
        Pagina, on_delete=models.DO_NOTHING,
        verbose_name="pagina",
        help_text="pagina",
        blank=True, null=True
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["id"]
        verbose_name = "Documento",
        verbose_name_plural = "Documento"

    def __str__(self):
        return self.titulo
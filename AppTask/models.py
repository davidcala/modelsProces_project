from django.db import models

# Create your models here.
from django.utils.translation import ugettext_lazy as _

class Entity(models.Model):
    """
    """

    STATUS = (("Inactivo", "Inactivo"), ("Activo", "Activo"))
    status = models.CharField(verbose_name=_("Estado"), max_length=20, choices=STATUS, default=1)
    created_date = models.DateTimeField(verbose_name=_("Fecha Creación"), auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name=_("Fecha Actualización"), auto_now=True)

    class Meta:
        abstract = True


class Category(Entity):
    """
    """

    name = models.CharField(verbose_name=_("Nombre"), max_length=50)
    description = models.TextField(verbose_name=_("Descripción"), default='', blank=True)


    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Tag(Entity):
    """
    """

    name = models.CharField(verbose_name=_("Nombre"), max_length=50)
    description = models.TextField(verbose_name=_("Descripción"), default='', blank=True)

    class Meta:
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Etiquetas'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Product(Entity):
    """
    """

    product_code = models.CharField(verbose_name=_("Código Producto"), max_length=50, null=True, blank=True)
    name = models.CharField(verbose_name=_("Nombre"), max_length=50, unique=True)
    category = models.ForeignKey(Category, verbose_name=_("Categoría"), on_delete=models.CASCADE,
                                 related_name="product_category")
    price = models.DecimalField(_("Precio"), max_digits=7, decimal_places=2, default=0.00)
    stock = models.PositiveIntegerField(verbose_name=_("Stock"), default=0)
    tags = models.ManyToManyField(Tag, related_name='product_tags')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
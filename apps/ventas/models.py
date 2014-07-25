from django.db import models

# Create your models here.


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    cantidad = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.nombre

from django.db import models

# Create your models here.
# ctrl+shif+p = auto identar


class Insumo(models.Model):
    nombre = models.CharField(max_length=50)
    #cantidad = models.IntegerField()

    def __unicode__(self):
        return self.nombre

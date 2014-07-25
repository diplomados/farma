from django.contrib import admin

# Register your models here.
from apps.ventas.models import Producto


class ProductoAdmin(admin.ModelAdmin):

    """docstring for ProductoAdmin"""
    search_fields = ('nombre',)
    list_display = ('nombre', 'cantidad',)
    list_per_page = 2

admin.site.register(Producto, ProductoAdmin)

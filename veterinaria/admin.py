from django.contrib import admin
from .models import cliente, atencion
# Register your models here.

@admin.register(cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombre', 'apellido', 'correo', 'telefono', 'monto')
    search_fields = ('rut', 'nombre', 'apellido', 'correo', 'telefono') 

    def monto_formateado(self, obj):
        return f"${obj.monto:,.0f}".replace(",",".")


@admin.register(atencion)
class AtencionAdmin(admin.ModelAdmin):
    list_display = ('id_atencion', 'fecha', 'hora', 'motivo', 'cliente')
    search_fields = ('id_atencion', 'fecha', 'hora', 'motivo', 'cliente__nombre', 'cliente__apellido')




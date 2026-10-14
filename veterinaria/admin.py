from django.contrib import admin
from .models import cliente, atencion
# Register your models here.
admin.site.site_header = "Veterinaria Admin"
admin.site.site_title = "Veterinaria Admin Portal"
admin.site.index_title = "Bienvenido a Veterinaria Admin Portal"

@admin.register(cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombre', 'apellido', 'correo', 'telefono', 'monto_formateado')
    search_fields = ('rut', 'nombre', 'apellido', 'correo', 'telefono')
    list_filter = ('nombre', 'apellido')
    ordering = ('nombre', 'apellido')
    search_fields = ('rut', 'nombre', 'apellido', 'correo', 'telefono')

    def monto_formateado(self, obj):
        return f"${obj.monto:,.0f}".replace(",",".")


@admin.register(atencion)
class AtencionAdmin(admin.ModelAdmin):
    list_display = ('id_atencion', 'fecha', 'hora', 'motivo', 'cliente')
    search_fields = ('id_atencion', 'fecha', 'hora', 'motivo', 'cliente__nombre', 'cliente__apellido')
    list_filter = ('fecha', 'hora', 'cliente__nombre', 'cliente__apellido')
    search_fields = ('id_atencion', 'fecha', 'hora', 'motivo', 'cliente__nombre', 'cliente__apellido')
    



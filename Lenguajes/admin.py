from django.contrib import admin
from .models import DatosPersonales, Cuestionario

# Register your models here.
class CuestionarioAdmin(admin.ModelAdmin):
	list_display = ('Fecha','Calificacion',)
	list_filter = ('Fecha','Calificacion',)
	

class DatosPersonalesAdmin(admin.ModelAdmin):
	list_display = ('Nombre', 'Ap_Paterno',)
	list_filter = ('Nombre', 'Ap_Paterno',)
	

admin.site.register(DatosPersonales, DatosPersonalesAdmin)
admin.site.register(Cuestionario, CuestionarioAdmin)

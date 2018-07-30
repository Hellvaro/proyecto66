from django.contrib import admin
from apps.appmusicoenvivo.models import Banda,Musico,Comuna,Local,Tipo_Local,Estilo,Instrumento,Region
# Register your models here.

admin.site.register(Banda)
admin.site.register(Musico)
admin.site.register(Comuna)
admin.site.register(Local)
admin.site.register(Tipo_Local)
admin.site.register(Estilo)
admin.site.register(Instrumento)
admin.site.register(Region)

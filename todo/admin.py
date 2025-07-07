from django.contrib import admin
from .models import Tarea
#aqui se registra el modelo en el administrado
admin.site.register(Tarea)

#con esto se pueden ver las tareas en el panel dee administracion
#con este modelo se pueden crear editar y eliminar tareas

# Register your models here.

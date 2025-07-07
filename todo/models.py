from django.db import models

#aqui se creo el modelo y la tabla tareas con un solo campo de 
# tipo charfield, se migra el modelo, y se crean las migraciones
#las migraciones van quedando en el pycache que se crea en la carpeta


class Tarea(models.Model):
    tarea=models.CharField(max_length=100)
    def __str__(self):
        return self.tarea

# Create your models here.

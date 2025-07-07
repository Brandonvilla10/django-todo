from django.shortcuts import render, redirect
from .models import Tarea
from .forms import TareaForm



# Create your views here.

def home(request):
    tareas = Tarea.objects.all() #conexion al modelo para traer data
    context = {'tareas': tareas} #coloco el modelo en una variable
    return render(request, 'todo/home.html', context) #aqui mando el modelo a la vista


def agregar(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TareaForm()
    context = {'form': form}
    return render(request, 'todo/agregar.html', context)

# AAAAA aca se colocan las rutas de las vistas, osea esto actua de controlador
def eliminar(request, tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    tarea.delete()
    return redirect('home')


def editar(request, tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TareaForm(instance=tarea)
    context = {'form': form}
    return render(request, 'todo/editar.html', context)

from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404, redirect, render

from catalogo.forms.libro_from import LibroForm
from catalogo.models import Libro


@login_required
@permission_required('catalogo.view_libro', raise_exception=True)
def libro_list(request):
    libros = Libro.objects.select_related('categoria').all()
    return render(request, 'libros/libro_list.html', {'libros': libros})


@login_required
@permission_required('catalogo.add_libro', raise_exception=True)
def create_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Libro creado exitosamente.')
            return redirect('libro_list')
    else:
        form = LibroForm()
    return render(request, 'libros/formulario.html', {'form': form})


@login_required
@permission_required('catalogo.change_libro', raise_exception=True)
def update_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            messages.success(request, 'Libro actualizado exitosamente.')
            return redirect('libro_list')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'libros/formulario.html', {'form': form})


@login_required
@permission_required('catalogo.delete_libro', raise_exception=True)
def delete_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        libro.delete()
        messages.success(request, 'Libro eliminado exitosamente.')
        return redirect('libro_list')
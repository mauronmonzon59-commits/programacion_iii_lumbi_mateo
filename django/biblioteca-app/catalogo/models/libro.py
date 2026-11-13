from django.db import models
from .categorias import Categoria
from .autor import Autor

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    fecha_publicacion = models.DateField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    isbn = models.CharField(max_length=100)
    autores = models.ManyToManyField(Autor, blank=True, related_name='libros')

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = "libros"
        verbose_name = "libro"
        ordering = ['titulo']
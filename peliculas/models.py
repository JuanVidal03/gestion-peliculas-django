from django.db import models

# modelo para las categorias de las pelculas
class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    
    def __str__(self) -> str:
        return self.nombre
    
# modelo de pelliculas
class Pelicula(models.Model):
    codigo = models.CharField(max_length=9)
    titulo = models.CharField(max_length=100)
    protagonista = models.CharField(max_length=50)
    duracion = models.IntegerField()
    resumen = models.CharField(max_length=2000)
    foto = models.ImageField(upload_to=f"media/", null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
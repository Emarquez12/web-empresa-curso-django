from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titulo')
    description = models.TextField(verbose_name='Descripcion')
    image = models.ImageField(upload_to='projects/', verbose_name='Imagen')
    url = models.URLField(blank=True, null=True, verbose_name='URL')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    updated = models.DateTimeField(auto_now=True, verbose_name='Modificado el')
    
    class Meta:
        verbose_name="projecto"
        verbose_name_plural="Projectos"
        ordering = ["-created"] #del mas nuevo al mas viejo
    
    def __str__(self):
        return self.title
    
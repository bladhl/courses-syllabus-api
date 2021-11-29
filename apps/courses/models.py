from django.db import models

from apps.users.models import User


# Create your models here.
class CourseCategory(models.Model):
  code = models.CharField('Código', max_length=4, unique=True)
  description = models.CharField('Descripción', max_length=50, null = False, blank = True)

  class Meta:
    verbose_name = 'Categoria'
    verbose_name_plural = 'Categorias'
    
  def __str__(self):
    return self.code

  
class Couse(models.Model):
  name = models.CharField('Nombre', max_length=255)
  credits = models.PositiveSmallIntegerField('Creditos')
  category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE, verbose_name='Categoria del Curso')
  professor = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = 'Docente del Curso', null=True, blank=True)

  class Meta:
    verbose_name = 'Curso'
    verbose_name_plural = 'Cursos'
  
  def __str__(self):
    return self.name
from django.db import models

# Create your models here.
class BaseModel(models.Model):
  
  id = models.AutoField(primary_key=True)
  is_active =models.BooleanField('Estado', default=True)
  created_at = models.DateField('Fecha de creación', auto_now=False, auto_now_add=True)
  modified_at = models.DateField('Fecha de modificación', auto_now=True, auto_now_add=False)
  deleted_at = models.DateField('Fecha de eliminación', auto_now=True, auto_now_add=False)
  
  class Meta:
    
    abstract = True
    verbose_name = 'Modelo Base'
    verbose_name_plural = 'Modelos Base'

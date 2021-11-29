from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

# Create your models here.
class UserManager(BaseUserManager):
  
  def create_user(self, code, id_card, name, last_name1, last_name2, email, password, **extra_fields):
    
    if not code: raise ValueError('The code must be set')
    if not email: raise ValueError('The email must be set')
    
    email = self.normalize_email(email)
    user = self.model(code=code, id_card=id_card, name=name, last_name1=last_name1, last_name2=last_name2, email=email, **extra_fields)
    user.set_password(password)
    user.save(using=self.db)
    
    return user
    
  def create_superuser(self, code, id_card, name, last_name1, last_name2, email, password, **extra_fields):
    
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)
    extra_fields.setdefault('is_active', True)
    
    if extra_fields.get('is_staff') is not True:
      raise ValueError(_('Superuser must have is_staff=True'))
    if extra_fields.get('is_superuser') is not True:
      raise ValueError(_('Superuser must have is_superuser=True'))
    
    return self.create_user(code, id_card, name, last_name1, last_name2, email, password, **extra_fields) 


class User(AbstractBaseUser, PermissionsMixin):
  
  CATEGORY_CHOICES = [('Contratado','Contratado'), ('Nombrado','Nombrado')]
  
  code = models.CharField('Código', max_length=6, unique=True)
  id_card = models.CharField('DNI', max_length=8, unique=True)
  name = models.CharField('Nombres', max_length=255, blank=True, null=True)
  last_name1 = models.CharField('Apellido Paterno', max_length=255, blank=True, null=True)
  last_name2 = models.CharField('Apellido Materno', max_length=255, blank=True, null=True)
  email = models.EmailField('Correo Electrónico', max_length=255, unique=True)
  phone = models.CharField('Número de celular', max_length=9)
  category = models.CharField('Categoría', max_length=10, choices=CATEGORY_CHOICES)
  image = models.ImageField('Imagen de perfil', upload_to='perfil/', max_length=255, blank=True, null=True)
  is_active = models.BooleanField('Activo', default=True)
  is_staff = models.BooleanField('Administrador', default=False)
  objects = UserManager()

  class Meta:
    verbose_name = 'Usuario'
    verbose_name_plural = 'Usuarios'
  
  USERNAME_FIELD = 'code'
  REQUIRED_FIELDS = ['id_card', 'name', 'last_name1', 'last_name2', 'email']
  
  def __str__(self):
    return f'{self.name} {self.last_name1} {self.last_name2}'
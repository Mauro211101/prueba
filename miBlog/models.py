from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
#from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    nombre_circuito = models.CharField(max_length=35)
    descripcion_corta = models.CharField(max_length=35)
    descripcion_circuito = models.CharField(max_length=500)
    circuit_image = models.ImageField(upload_to="posts",null=True,blank=True)
    post_author = models.ForeignKey(to=User,on_delete=models.CASCADE, related_name="publisher")
    fecha_de_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.id} -- {self.nombre_circuito} -- {self.descripcion_corta}"
        

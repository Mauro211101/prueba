from django.db import models
from django.contrib.auth.models import User
#from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    circuit_name = models.CharField(max_length=35)
    circuit_description = models.CharField(max_length=250)
    #circuit_image = models.ImageField(upload_to="posts",null=true,blank=True)
    post_author = models.ForeignKey(to=User,on_delete=models.CASCADE, related_name="publisher")
    date_created = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return f"{self.id} -- {self.circuit_name} -- {self.circuit_description}"
        

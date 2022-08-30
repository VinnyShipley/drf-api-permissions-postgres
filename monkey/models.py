from django.db import models
from django.contrib.auth import get_user_model

class Monkey(models.Model):
  owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  name = models.CharField(max_length=256)
  tude = models.CharField(max_length=256)
  birth_info = models.DateTimeField(auto_now_add=True)
  updated_info = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return self.name

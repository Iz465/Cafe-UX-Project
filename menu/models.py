from django.db import models

# Create your models here.
class Menu(models.Model):
  name = models.CharField(max_length=255)
  price = models.DecimalField(decimal_places=2, max_digits=6)
  description = models.CharField(max_length=255)
  image_url = models.CharField(max_length = 2550)

from django.db import models

class Employ(models.Model):
  name = models.CharField(max_length=255)
  income = models.IntegerField()
  description = models.CharField(max_length=255)
  image_url = models.CharField(max_length = 2083)


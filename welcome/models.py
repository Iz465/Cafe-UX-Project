from django.db import models


class Welcome(models.Model):
  name = models.CharField(max_length = 255)
  description = models.CharField(max_length = 255)
  image_url = models.CharField(max_length = 2083)



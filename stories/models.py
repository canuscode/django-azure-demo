from django.db import models

class Stories(models.Model):
    image = models.ImageField('images/')
    summary = models.CharField(max_length=255)

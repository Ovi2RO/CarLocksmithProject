from django.db import models

class Testimony(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()

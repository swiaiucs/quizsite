from django.db import models

# Create your models here.

class Quiz(models.Model):
	name = models.CharField(max_lenght=100)
	name = models.SlugField(max_lenght=100)
	description = models.TextField()
from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name= models.TextField(max_length= 30)
    description = models.TextField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    created_at = models.DateTimeField()
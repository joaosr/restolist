from django.db import models

# Create your models here.
class Restaurant(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50)
    address = models.TextField()
    phone = models.CharField(max_length=30)
    website = models.URLField(max_length=200)
    created_at = models.DateTimeField('Created at', auto_now_add=True)

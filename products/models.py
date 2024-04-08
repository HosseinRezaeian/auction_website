from django.db import models

# Create your models here.
class ProductOrService(models.Model):
    title=models.CharField()
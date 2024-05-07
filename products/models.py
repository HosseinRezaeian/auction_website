from django.db import models
from django.contrib.auth.models import User
from slugify import slugify


# Create your models here.
class ProductOrService(models.Model):
    title = models.CharField(max_length=60)
    slug = models.CharField(blank=True,max_length=255)
    base_price = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.TextField()
    auctioneer = models.ForeignKey(User, on_delete=models.CASCADE)
    type_value = [('public sale', 'public sale'),
                  ('English auction', 'English auction')]
    type = models.CharField(choices=type_value, max_length=40)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Picture(models.Model):
    parent = models.ForeignKey(ProductOrService, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='pictures/')

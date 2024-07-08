from django.db import models
from django.contrib.auth.models import User
from slugify import slugify
from django.conf import settings
import datetime
from django.utils import timezone


# Create your models here.
class ProductOrService(models.Model):
    title = models.CharField(max_length=60)
    slug = models.SlugField(blank=True, max_length=60)
    base_price = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.TextField()
    first_pic = models.ImageField(blank=True, null=True, upload_to='pictures')
    auctioneer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    type_value = [('public sale', 'public sale'),
                  ('English auction', 'English auction')]
    type = models.CharField(choices=type_value, max_length=40)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def is_future_date(self):
        if self.start_date <= timezone.now() <= self.end_date:
            return 'in_auc'
        if self.start_date > timezone.now():
            return 'can'
        if self.end_date < timezone.now():
            return 'cant'

    def __str__(self):
        return self.title


class Picture(models.Model):
    parent = models.ForeignKey(ProductOrService, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='pictures')

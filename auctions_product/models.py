from django.db import models
from django.conf import settings


# Create your models here.


class Auctions_user_product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey('products.ProductOrService', on_delete=models.CASCADE)
    price = models.IntegerField(blank=False, null=False)
    datetime = models.DateTimeField(blank=False, null=False)
    is_win = models.BooleanField(default=False, )

    def __str__(self):
        return "{}-{}".format(self.user.name, self.product.title)

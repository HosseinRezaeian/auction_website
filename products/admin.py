from django.contrib import admin
from .models import ProductOrService, Picture


# Register your models here.


class PictureInline(admin.TabularInline):  # You can use admin.StackedInline for a different layout
    model = Picture
    extra = 1


class ProductOrServiceAdmin(admin.ModelAdmin):
    inlines = [PictureInline]


admin.site.register(ProductOrService, ProductOrServiceAdmin)

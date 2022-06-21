from django.contrib import admin
from numpy import product

# Register your models here.
from .models import Product
admin.site.register(Product)
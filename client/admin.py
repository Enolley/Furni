from django.contrib import admin
from .models import Product, Testimonial, Blog
# Register your models here.
admin.site.register(Product)
admin.site.register(Testimonial)
admin.site.register(Blog)
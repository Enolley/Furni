from django.db import models
from django.utils import timezone


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=60, blank=False, null=False)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to="uploads/products", default="uploads/products/profile.png")

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name = models.CharField(max_length=60, blank=False, null=False)
    testimonial = models.TextField()
    post = models.CharField(max_length=150, blank=False, null=False)
    image = models.ImageField(upload_to="uploads/testimonials", default="uploads/testimonials/profile.png")

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=60, blank=False, null=False)
    name = models.CharField(max_length=60, blank=False, null=False)
    image = models.ImageField(upload_to="uploads/blogs", default="uploads/blogs/profile.png")
    created_at = models.DateTimeField(default=timezone.now)
    content = models.TextField(null=False, default="Blog")

    def __str__(self):
        return self.title

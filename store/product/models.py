from django.db import models

class Material(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Dimension(models.Model):
    name = models.CharField(max_length=100, unique=True)  # e.g. "10x20x15 cm"

    def __str__(self):
        return self.name

class Weight(models.Model):
    name = models.CharField(max_length=50, unique=True)  # e.g. "2 kg"

    def __str__(self):
        return self.name

class Feature(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=100, unique=True)  # e.g. "Red", "Blue"

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=100, unique=True, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    materials = models.ManyToManyField(Material, blank=True, related_name='products')
    dimensions = models.ManyToManyField(Dimension, blank=True, related_name='products')
    weights = models.ManyToManyField(Weight, blank=True, related_name='products')
    features = models.ManyToManyField(Feature, blank=True, related_name='products')
    colors = models.ManyToManyField(Color, blank=True, related_name='products')

    def __str__(self):
        return self.name


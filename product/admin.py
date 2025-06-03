from django.contrib import admin
from .models import Product, Material, Dimension, Weight, Feature, Color

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    search_fields = ['name']

@admin.register(Dimension)
class DimensionAdmin(admin.ModelAdmin):
    search_fields = ['name']

@admin.register(Weight)
class WeightAdmin(admin.ModelAdmin):
    search_fields = ['name']

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    search_fields = ['name']

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    search_fields = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'sku', 'price', 'is_active', 'is_featured', 'created_at', 'updated_at']
    list_filter = ['is_active', 'is_featured', 'created_at']
    search_fields = ['name', 'sku']
    filter_horizontal = ['materials', 'dimensions', 'weights', 'features', 'colors']
    readonly_fields = ['created_at', 'updated_at']


from django.contrib import admin
from .models import *
# Register your models here.

class Product_Images(admin.TabularInline):
    model = Product_Image

class Additonal_Informations(admin.TabularInline):
    model = Additional_Information

class Product_Admin(admin.ModelAdmin):
    inlines = (Product_Images, Additonal_Informations)
    list_display = ('product_name', 'categories', 'section')
    list_editable = ('categories', 'section')


admin.site.register(Slider)
admin.site.register(Banner_Area)
admin.site.register(Main_Category)
admin.site.register(Category)
admin.site.register(Sub_Category)
admin.site.register(Section)
admin.site.register(Product, Product_Admin)
admin.site.register(Product_Image)
admin.site.register(Additional_Information)
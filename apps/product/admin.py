from django.contrib import admin
from .models import *

@admin.register(Product_model)
class Product_admin(admin.ModelAdmin):

    list_display=('title','short_des','description',
    'image','registered','updated','user_register','view_number',
    'published','price','order_quantity')

    readonly_fields=('order_quantity','view_number')

    search_fields=('title','published')

    prepopulated_fields={'slug':('title',)}


 


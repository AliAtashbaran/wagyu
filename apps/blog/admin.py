from django.contrib import admin
from apps.blog.models import *

@admin.register(Recipe_model)
class Recipe_admin(admin.ModelAdmin):
    list_display=('title','short_des','description','image',
    'registered','uppdated','slug','published','user_register',
    'view_counter','like_counter')

    readonly_fields=('view_counter','like_counter')

    prepopulated_fields={'slug':('title',)}

    search_fields=['published',]

# ----------------------------------

@admin.register(Recipe_like_model)
class Recipe_like_admin(admin.ModelAdmin):
    list_display=('recipe','user','time')

from django.contrib import admin
from .models import Contact_us_model

@admin.register(Contact_us_model)
class Contact_us_admin(admin.ModelAdmin):
    list_display=('fullname','email','phone','category','description')
    readonly_fields=('registered',)


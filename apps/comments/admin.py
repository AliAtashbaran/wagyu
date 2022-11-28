from django.contrib import admin
from apps.comments.models import *

@admin.register(Comment_model)
class Comments_Admin(admin.ModelAdmin):
    list_display=('post','name','body','active','like_count','time','user','email')
    readonly_fields=('like_count','user','post','name','body','email')
    search_fields=['active',]


@admin.register(Comment_like)
class Comments_like_Admin(admin.ModelAdmin):
    list_display=('comment','user','time')
    # readonly_fields=('comment',)

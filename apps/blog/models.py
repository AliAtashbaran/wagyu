from django.db import models
from django.contrib.auth.models import User
import datetime

def image_path(instance,file_name):
    name=file_name.split('.')[0]
    ext=file_name.split('.')[-1]
    milisecond=datetime.datetime.utcnow().strftime('%f')
    return f'images/blog/{instance.title}/{name}-{milisecond}.{ext}'

class Recipe_model(models.Model):

    title=models.CharField(max_length=50,verbose_name='Title')
    short_des=models.TextField(verbose_name='Short Description')
    description=models.TextField(verbose_name='Description')
    image=models.ImageField(upload_to=image_path,verbose_name='Image')
    registered=models.DateTimeField(auto_now_add=True,verbose_name='Registered')
    uppdated=models.DateTimeField(auto_now=True,verbose_name='Uppdated')
    slug=models.SlugField(verbose_name='Slug')
    published=models.BooleanField(default=False,verbose_name='Published')
    user_register=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,verbose_name='User Registered')
    view_counter=models.PositiveIntegerField(default=0,verbose_name='Views')
    like_counter=models.PositiveIntegerField(default=0,verbose_name='Likes')
    
    def __str__(self):
        return f'{self.title}'
# ------------------------------

class Recipe_like_model(models.Model):
    recipe=models.ForeignKey(Recipe_model,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}"


from django.db import models
from apps.blog.models import Recipe_model 
from django.contrib.auth.models import User



class Comment_model(models.Model):
    post=models.ForeignKey(Recipe_model ,on_delete=models.CASCADE,related_name='comments')
    name=models.CharField(verbose_name='Name',blank=True,null=True,max_length=100)
    body=models.TextField(verbose_name='Body',blank=True,null=True)
    active=models.BooleanField(default=False,verbose_name='Active')
    like_count=models.PositiveIntegerField(default=0)
    time=models.DateTimeField(auto_now_add=True)
    user=models.CharField(max_length=30,verbose_name='User')
    email=models.EmailField(max_length=100,verbose_name='Email',default='registered_user')

    def __str__(self):
        return f"{self.post.title}{self.name}"

class Comment_like(models.Model):
    comment=models.ForeignKey(Comment_model,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}"
    
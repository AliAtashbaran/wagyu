from django.db import models
from django.contrib.auth.models import User



class Product_model(models.Model):

    brand=models.CharField(max_length=30)
    title=models.CharField(max_length=100)
    short_des=models.TextField()
    description=models.TextField()
    image=models.CharField(default='images/product/',max_length=100)
    slug=models.SlugField(max_length=100,unique=True)
    registered=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    user_register=models.ForeignKey(User,on_delete=models.CASCADE)
    view_number=models.IntegerField(default=0)
    published=models.BooleanField(default=False)
    price=models.CharField(max_length=10)
    order_quantity=models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.title}"

# -----------------------------------

class Product_feature(models.Model):
    feature_name=models.CharField(max_length=100)
    feature_value=models.CharField(max_length=100)
    product=models.ForeignKey(Product_model,on_delete=models.CASCADE,related_name='feature')
    user_register=models.ForeignKey(User,on_delete=models.CASCADE)


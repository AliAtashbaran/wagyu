
from rest_framework import serializers

from apps.product.models import Product_feature, Product_model


class Product_serializer(serializers.ModelSerializer):

    feature=serializers.SerializerMethodField()
    class Meta:
        model=Product_model
        fields=('brand','title','short_des','description','price','user_register','slug','feature')

    def create(self,validated_data):
        return Product_model.objects.create(**validated_data)
# ------------------------------
    def get_feature(self,obj):
        res=obj.feature.all()
        return Product_feature_serializer(instance=res,many=True).data

class Product_feature_serializer(serializers.ModelSerializer):
    class Meta:
        model=Product_feature
        fields=('feature_name','feature_value','user_register','product')

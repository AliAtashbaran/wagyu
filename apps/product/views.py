
from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from .serializer import*

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from .models import *
from django.contrib.auth.models import User
from custom_permission import Custom_Permission

class Product_detail_view(DetailView):

    model=Product_model
    fields="__all__"
    template_name='product/product.html'
    context_object_name='product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["slug"]=self.kwargs 
        
        product=Product_model.objects.get(slug=self.kwargs['slug'])
        product.view_number+=1
        product.save()
        return context

# ----------------------------------    
class Show_product_details_api(APIView):

    def get(self,request):
        product=Product_model.objects.all()
        ser_data=Product_serializer(instance=product,many=True)
        return Response(data=ser_data.data,status=status.HTTP_200_OK)


class Add_product_api(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):

        ser_data=Product_serializer(data=request.POST)
        if ser_data.is_valid():
            ser_data.create(ser_data.validated_data)

            return Response(data=ser_data.data,status=status.HTTP_201_CREATED)
        else:
            return Response(ser_data.errors,status=status.HTTP_400_BAD_REQUEST)
# ------------------------------

# to create Token for all existing users in data base
@api_view(['GET'])
def create_token_forAll(request):
    for user in User.objects.all():
        Token.objects.get_or_create(user=user)
    return Response(status=status.HTTP_200_OK)

# ------------------------------------

class Delete_product(APIView):
    permission_classes=[Custom_Permission]
    def delete(self,request,pk):
        try:
            product=Product_model.objects.get(pk=pk)
            self.check_object_permissions(request,product)
            product.delete()
            return Response('deletion completed')
        except Product_model.DoesNotExist:
            return Response('Item not found')

# -------------------------------

class Add_product_feature(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        ser_data=Product_feature_serializer(data=request.POST)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data,status=status.HTTP_201_CREATED)
        
        else: 
            return Response(ser_data.errors,status=status.HTTP_400_BAD_REQUEST)
    # ------------------------------------
    







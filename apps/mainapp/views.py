
import os


from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseNotFound
from django.conf import settings
from django.views import View
from django.views.generic.edit import UpdateView
from django.views.generic import ListView
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.core.mail import EmailMultiAlternatives, send_mail




from apps.contactus.models import Contact_us_model
from apps.product.models import Product_model 

from .forms import * 
from .models import *

def username_appearance(request):
    context={}
    if request.user.is_authenticated:
        return {'username':request.user.username}
    return context
# ---------------------------

def media_admin(request):

    return {'media_url':settings.MEDIA_URL}
# =======================
def send_email(subject,message,to):
    host_email=settings.EMAIL_HOST

    print(send_mail(subject,message,host_email,to))


class Index(ListView):

    model=Product_model
    fields='__all__'
    template_name='maintemplate.html'
    context_object_name='product'
# =======================


class User_registration(View):

    def get(self,request,*args,**kwargs):
        
        form=User_registration_form()
        return render(request,'mainapp/forms/user_reg.html',{'form':form})

    def post(self,request,*args,**kwargs):
        form=User_registration_form(request.POST)

        if form.is_valid():
            data=form.cleaned_data
            user=User(
                username=data.get('username'),
                email=data.get('email')
            )
            user.set_password(data.get('password1'))
            user.save()
            message='Your registered successfully'
            messages.success(request,message,'success')
            subject='The Wagyu House registration'
            message=f'Welcomo the "The Wagyu House" {user.username} please feel free to contact us for any queries regarding whole sales.'
            send_email(subject,message,['ali_atashbaran@yahoo.com'])
            
            return redirect('/')
        else:
            message='Your information is not valid.'
            messages.error(request,message,'warning')
            return render(request,'mainapp/forms/user_reg.html',{'form':form})

#---------------------------------

class Login(View):

        def get(self,request,*args,**kwargs):
        
            form=Login_form()
            return render(request,'mainapp/forms/login.html',{'form':form})

        def post(self,request,*args,**kwargs):
            form=Login_form(request.POST)
            if form.is_valid():
                
                data=form.cleaned_data
                user=authenticate(username=data['username'],password=data['password'])
                
                if user is not None:
                    login(request,user)
                    message=f'Welcome back dear '+data['username']
                    messages.success(request,message,'success')
                    return redirect('/')
                else:
                    message='Username or password is not correct'
                    messages.warning(request,message,'warning')
            return render(request,'mainapp/forms/login.html',{'form':form})

# ----------------------------------

class Logout(View):
    def get(self,request,*args,**kwargs):
        
        logout(request)
        messages.success(request,'Your logout is successful','success')
        return redirect('/')    
# --------------------------------

class User_panel(UpdateView):

    model=User
    context_object_name='form'
    fields=['first_name','last_name','username','email']
    template_name='mainapp/forms/user_panel.html'
    success_url='/'

    def get_context_data(self, **kwargs):
        form=User_panel_form()
        context = super().get_context_data(**kwargs)
        context["pk"] =self.kwargs 
        return context
       
# ----------------------------------

def search(request):
    if request.method=="POST":
        searched=request.POST['searched']
        res=Product_model.objects.filter(description__icontains=searched)
        res2=Product_model.objects.filter(title__icontains=searched)
        return render(request,'mainapp/forms/search.html',{'searched':searched,'res':res,'res2':res2})

# ---------------------------------

def download_pdf(request):

    fss=FileSystemStorage()
    file_path='pdf/wagyu.pdf'
    if fss.exists(file_path):
        with fss.open(file_path) as download_pdf:
            result=HttpResponse(download_pdf,content_type='application/pdf')
            result['Content-Disposition']='inline;filename=wagyu.pdf'
            return result
    else: 
        # return HttpResponseNotFound('Sorry the file you are trying to download is not currently available.')
        message='Sorry the file you are trying to download is not currently available.'
        messages.error(request,message)
        return redirect('/')

# ---------------------------------

def about_us(request):
    return render(request,'mainapp/about_us.html')

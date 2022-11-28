from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.views.generic import View
from django.views.generic.edit import CreateView

from apps.contactus.forms import*
from .models import*

# class Conact_us_view(CreateView):
#     model=Contact_us_model
#     fields='__all__'
#     context_object_name='form'
#     template_name='contact_us/contact_us.html'
#     success_url='/'

class Conact_us_view(View):

    def get(self,request,*args,**kwargs):
        form =Contact_us_form()
        return render(request,'contact_us/contact_us.html',{'form':form})

    def post(self,request,*args,**kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form =Contact_us_form(request.POST)
            if form.is_valid():
                name=form.cleaned_data['fullname']
                form.save()
                return JsonResponse({'name':name})
            else:
                return render(request,'contact_us/contact_us.html',{'form':form})
        else:
            error=form.errors.as_json()
            return JsonResponse(error,status=400) 
# -------------------------


        
          
        


        


from django.shortcuts import render,redirect


from apps.comments.forms import Comment_form
from apps.comments.models import Comment_model
from apps.product.models import Product_model 



# def comment_view(request,id):
    
#     if request.method=="GET":
        
#         form=Comment_form()
#         return render(request,'comment/comment.html',{'form':form})
#     else:
#         form=Comment_form(request.POST)
#         if form.is_valid():
#             product=Product_model.objects.get(id=id)
#             data=form.cleaned_data
#             Comment_model.objects.create(
#                 post=product,
#                 name=data['name'],
#                 body=data['body']
#             )
#             return redirect('product:product_details',slug=product.slug)
#         else:
#             return render(request,'comment/comment.html',{'form':form})
            

            
        

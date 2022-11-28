from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import View
from django.http import HttpResponse,HttpResponseForbidden


from apps.blog.models import *
from apps.comments.forms import * 
from apps.comments.models import Comment_model,Comment_like
from apps.blog.models import Recipe_like_model


class Recipe_list_view(ListView):
    model=Recipe_model
    fields="__all__"
    template_name='blog/recipe_list.html'
    context_object_name='recipe'
# ---------------------

# This view class consist of 2 function, recipe details and comments
class Recipe_detail_comments_view(View):
    
    def get(self,request,*args,**kwargs):
        list_recipe_liked_id=[]
        global recipe
        recipe=Recipe_model.objects.get(slug=kwargs['slug'])
        recipe.view_counter+=1
        recipe.save()
        if request.user.is_authenticated:
            list_recipe_liked=Recipe_like_model.objects.filter(user=request.user.id).values('recipe_id')
            list_recipe_liked_id=[recipe['recipe_id'] for recipe in list_recipe_liked]
            
        
        comments=Comment_form()
        global context
        context={
            'recipe':recipe,
            'form':comments,
            'recipe_liked_id':list_recipe_liked_id
        }
        return render(request,'blog/recipe_detail.html',context)
    
    def post(self,request,*args,**kwargs):
        form=Comment_form(request.POST)
        user='guest'
        if request.user.is_authenticated:
            user=request.user.username
        if form.is_valid():
            data=form.cleaned_data 
            Comment_model.objects.create(
                post=recipe,
                name=data['name'],
                body=data['body'],
                user=user,
                email=data['email']
            )
            return redirect('blog:recipe_detail',slug=kwargs['slug']) 
        return render(request,'blog/recipe_detail.html',context)

# ------------------------------

def comment_like_view(request):
    if request.method=='GET':
        comment_id=request.GET['id']
        comment=Comment_model.objects.get(id=comment_id)
        if request.user.is_authenticated:
            comment.like_count+=1
            comment.save()
            Comment_like(comment=comment,user=request.user).save()
        
            return HttpResponse('Success')
        else:
            return HttpResponseForbidden
# ----------------------------------

def recipe_like_view(request):
    if request.method=='GET':
        recipe_id=request.GET['id']
        recipe=Recipe_model.objects.get(id=recipe_id)
        # list of user ids which they liked the same recipe(blog):
        recipe_like=Recipe_like_model.objects.filter(recipe_id=recipe)
        # check if there is no likes on this recipe(blog):
        if not recipe_like and request.user.is_authenticated:
                recipe.like_counter+=1
                recipe.save()
                Recipe_like_model(recipe=recipe,user=request.user).save()
            
                return HttpResponse('Success')
        # if user is loged in and has not liked the article before,
        # liked articles can not be liked again by the same user:
        elif request.user.is_authenticated:
            flag=False
            for recipe_id in recipe_like:
                if request.user.id == recipe_id.user.id:
                    flag=True
                    break
            if flag==False:
                recipe.like_counter+=1
                recipe.save()
                Recipe_like_model(recipe=recipe,user=request.user).save()
            
                return HttpResponse('Success')
            
            else:
                return HttpResponse("Unsuccess")
    else:
        return HttpResponse('Unaccepted method')


    




            
        
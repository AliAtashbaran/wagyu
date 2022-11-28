from django.urls import path
import apps.blog.views as view

app_name='blog'
urlpatterns = [
    path('recipe_list',view.Recipe_list_view.as_view(),name='recipe_list'),
    path('recipe_detail/<str:slug>/',view.Recipe_detail_comments_view.as_view(),name='recipe_detail'),
    path('comment_like/',view.comment_like_view),
    path('recipe_like/',view.recipe_like_view),
]

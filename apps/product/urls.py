from django.urls import path

import apps.product.views as view

# from rest_framework.authtoken import views as auth_token
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

app_name='product'
urlpatterns = [
    path('product_details/<str:slug>',view.Product_detail_view.as_view(),name='product_details'),

    # -----------------------------
    path('show_product_api/',view.Show_product_details_api.as_view()),
    path('add_product_api/',view.Add_product_api.as_view()),
    # path('get_token/',auth_token.obtain_auth_token),
    # path('create_token_forAll/',view.create_token_forAll),
    path('access_token/',TokenObtainPairView.as_view()),
    path('refresh_token/',TokenRefreshView.as_view()), 
    path('delete_product/<int:pk>/',view.Delete_product.as_view()),
    path('add_product_feature/',view.Add_product_feature.as_view()),
]

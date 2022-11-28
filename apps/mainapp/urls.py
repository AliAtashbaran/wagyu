from django.urls import path
import apps.mainapp.views as view

app_name='mainapp'
urlpatterns = [
    path('',view.Index.as_view(),name='home'),
    path('user_registration/',view.User_registration.as_view(),name='user_registration'),
    path('login/',view.Login.as_view(),name='user_login'),
    path('user_logout/',view.Logout.as_view(),name='user_logout'),
    path('user_panel/<int:pk>/',view.User_panel.as_view(),name='user_panel'),
    path('search/',view.search,name='search'),
    path('download_pdf/',view.download_pdf,name='download_pdf'),
    path('about_us/',view.about_us,name='about_us'),
]



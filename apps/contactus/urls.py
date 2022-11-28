from django.urls import path

from apps.contactus.views import Conact_us_view

app_name='contact_us'
urlpatterns = [
    path('contact_us/',Conact_us_view.as_view(),name='contact_us')
]

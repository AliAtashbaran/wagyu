from django import forms
from apps.contactus.models import Contact_us_model


class Contact_us_form(forms.ModelForm):
    class Meta:
        model=Contact_us_model
        fields='__all__'



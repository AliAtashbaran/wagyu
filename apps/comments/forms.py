from django import forms
from apps.comments.models import Comment_model


class Comment_form(forms.ModelForm):
    
    name=forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'user_formControl'}))
    body=forms.CharField(widget=forms.Textarea(attrs={'class':'user_formControl'}))
    email=forms.EmailField(required=False,widget=forms.EmailInput(attrs={'class':'user_formControl'}))
    
    class Meta:
        model=Comment_model
        fields=('name','body','email','like_count')


from string import ascii_uppercase
from string import punctuation

from django import forms 
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class User_registration_form(forms.ModelForm):
    
    username=forms.CharField(
        max_length=20,
        label='',
        widget=forms.TextInput(attrs={'placeholder':'Username','class':'user_formControl'}))
    
    email=forms.EmailField(
        max_length=100,
        label='',
        widget=forms.EmailInput(attrs={'placeholder':'Email Address','class':'user_formControl'}))
    
    
    
    password1=forms.CharField(
        min_length=8,
        max_length=20,
        label='',
        widget=forms.PasswordInput(attrs={'placeholder':'Password','class':'user_formControl'}))
    
    password2=forms.CharField(
        min_length=8,
        max_length=20,
        label='',
        widget=forms.PasswordInput(attrs={'placeholder':'Re-password','class':'user_formControl'}))

    class Meta:
        model=User
        fields=['username','email','password1','password2']


    def clean_password2(self):
        pass1=self.cleaned_data.get('password1')
        pass2=self.cleaned_data.get('password2')

        # password match validator:
        if pass1 and pass2 and pass1!=pass2:
            
            raise ValidationError('passwords are not matching.')
        
        #It checks if password include at least 1 uppercase and 1 simble.
        list=[]
        for char in pass2:
            if char in ascii_uppercase :
                list.append(char)
                break
        for char in pass2:
            if char in punctuation:
                list.append(char)
                break
        if len(list)<2:
            raise ValidationError('Password must contain at least 1 uppercase and 1 simble.')
        # ----------------------------


class Login_form(forms.Form):

    username=forms.CharField(
        max_length=20,
        label='',
        widget=forms.TextInput(attrs={'placeholder':'Username','class':'user_formControl'}))
    

    password=forms.CharField(
        min_length=8,
        max_length=20,
        label='',
        widget=forms.PasswordInput(attrs={'placeholder':'Password','class':'user_formControl'}))

# -----------------------------------------   

class User_panel_form(forms.ModelForm):

    first_name=forms.CharField(
            max_length=20,
            label='',
            widget=forms.TextInput(attrs={'placeholder':'First Name','class':'user_formControl'}))
        
    last_name=forms.CharField(
            max_length=50,
            label='',
            widget=forms.TextInput(attrs={'placeholder':'Last Name','class':'user_formControl'}))

    username=forms.CharField(
            max_length=20,
            label='',
            widget=forms.TextInput(attrs={'placeholder':'Username','class':'user_formControl'}))
            
    email=forms.CharField(
            max_length=100,
            label='',
            widget=forms.TextInput(attrs={'placeholder':'Email','class':'user_formControl'}))

    class Meta:
        model=User
        fields=['username','first_name','last_name','email']

    # ----------------------------------

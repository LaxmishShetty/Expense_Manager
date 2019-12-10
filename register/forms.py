from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(),label='Username')
    email = forms.CharField(widget=forms.EmailInput(attrs=dict(required=True,placeholder='E-mail')))
    password = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True,maxlength=15,placeholder='Password')))
    repassword= forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True,maxlength=15,placeholder='Re-enter password')))

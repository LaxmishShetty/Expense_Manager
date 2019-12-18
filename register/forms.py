from django import forms
import re
from ExpenseManager.models import UserProfileInfo,User
# class RegistrationForm(forms.Form):
#     username = forms.CharField(widget=forms.TextInput(),label='Username')
#     email = forms.CharField(widget=forms.EmailInput(attrs=dict(required=True,placeholder='E-mail')))
#     password = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True,maxlength=15,placeholder='Password')))
#     repassword= forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True,maxlength=15,placeholder='Re-enter password')))
#
#
#     def __init__(self,*args,**kwargs):
#         super(RegistrationForm, self).__init__(*args, **kwargs)
#         pass
#
#     def clean(self):
#         entered_password = self.cleaned_data.get('password')
#         entered_re_password = self.cleaned_data.get('repassword')
#         if entered_password != entered_re_password:
#             raise forms.ValidationError("Passwords don't match")
#
#         entered_username = self.cleaned_data.get('username')
#         if not any(char.isdigit() for char in entered_username):
#             raise forms.ValidationError("username should contain atleast 1 digit")
#
#         entered_email = self.cleaned_data.get('email')
#         if '@' not in entered_email:
#             raise forms.ValidationError("Wrong email format")
#
#         entered_password = self.cleaned_data.get('password')
#         if len(entered_password) < 6:
#             raise forms.ValidationError("Password should contain atleast 8 characters")
#         elif not any(char.isdigit() for char in entered_password):
#             raise forms.ValidationError("password should contain atleast 1 digit")
#         elif not any(char.isalpha() for char in entered_password):
#             raise forms.ValidationError("password should contain atleast 1 letter")
#         elif not any(char.isupper() for char in entered_password):
#             raise forms.ValidationError("Password should contain uppercase letters")
#         elif not any(char.islower() for char in entered_password):
#             raise forms.ValidationError("Password should contain lowercase letters")
#         elif not re.match(r'.*[\%\$\^\*\&\#\@\!\_\-\(\)\:\;\'\"\{\}\[\]].*', entered_password):
#             raise forms.ValidationError("Password should contain special characters")
#
#         return self.cleaned_data


# class LoginForm(forms.Form):
# #     username = forms.CharField(widget=forms.TextInput(),label="Username")

class UserLoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(),required=False)
    username = forms.CharField(widget=forms.TextInput(),required=False)
    repassword = forms.CharField(widget=forms.PasswordInput(),required=False)

    class Meta():
        model = User
        fields =('username','password','email')



class LoginForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(), required=False)
    username = forms.CharField(widget=forms.TextInput(), required=False)

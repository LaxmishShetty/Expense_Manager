from django import forms
from ExpenseManager.models import User

class FoodForm(forms.ModelForm):
    Name = forms.CharField(widget=forms.TextInput(),required=False)
    Expense = forms.IntegerField(widget=forms.NumberInput(),required=False)
    Datee = forms.DateField(widget=forms.DateInput(),required=False)

    class Meta:
        model = User
        fields = ()

    # def __init__(self, *args, **kwargs):
    #     self.request = kwargs.pop('request', None)
    #     super(FoodForm, self).__init__(*args, **kwargs)

    # def save(self, commit=True):
    #     if commit:
    #         self.request.user.save()
    #     return self.request.user





class PetrolForm(forms.Form):
    Expense = forms.IntegerField(widget=forms.NumberInput(), required=False)
    Datee = forms.DateField(widget=forms.DateInput(), required=False)


class ClothesForm(forms.Form):
    Cloth_Type = forms.CharField(widget=forms.TextInput(), required=False)
    Expense = forms.IntegerField(widget=forms.NumberInput(), required=False)
    Datee = forms.DateField(widget=forms.DateInput(), required=False)


class DaywiseForm(forms.Form):
    DayWiseDate = forms.DateField(widget=forms.DateInput(),required=False)
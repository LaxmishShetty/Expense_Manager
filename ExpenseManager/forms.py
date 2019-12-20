from django import forms
from ExpenseManager.models import User

class FoodForm(forms.Form):
    Name = forms.CharField(widget=forms.TextInput(),required=False)
    Expense = forms.IntegerField(widget=forms.NumberInput(),required=False)
    Datee = forms.DateField(widget=forms.DateInput(),required=False)




class PetrolForm(forms.Form):
    Expense = forms.IntegerField(widget=forms.NumberInput(), required=False)
    Datee = forms.DateField(widget=forms.DateInput(), required=False)


class ClothesForm(forms.Form):
    Cloth_Type = forms.CharField(widget=forms.TextInput(), required=False)
    Expense = forms.IntegerField(widget=forms.NumberInput(), required=False)
    Datee = forms.DateField(widget=forms.DateInput(), required=False)

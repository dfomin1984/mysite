from django import forms
from testapp.models import product

class addPostFormProduct(forms.Form):
    pName = forms.CharField(max_length=250,min_length=1,label='Название')
    pDescription = forms.CharField(widget=forms.Textarea(),required=False,label='Описание')
    pPrice = forms.DecimalField( max_digits=10, decimal_places=2,label='Цена')
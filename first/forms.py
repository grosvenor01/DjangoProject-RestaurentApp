from .models import order
from django import forms
class orderForm(forms.ModelForm):
    class Meta:
        model=order
        fields=['quantity',
               'user_name',
               'email',
               'adress',
               'phone']

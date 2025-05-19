from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        exclude = ['created_by']
        # fields = '__all__'
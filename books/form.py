from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class meta:
        model=Book
        fields='__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'published_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
from django import forms
from .models import Author

class GenerateQuoteForm(forms.Form):
    author = forms.ModelChoiceField(queryset=Author.objects.all())
from django import forms
from .models import Short_URL
class UrlForm(forms.ModelForm):
    class Meta:
        model=Short_URL
        fields=['long_url']
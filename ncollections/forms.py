from django import forms
from django.forms.widgets import HiddenInput

from .models import Ncollection, Nnft, Nattribute

class NcollectionForm(forms.ModelForm):
    class Meta:
        model = Ncollection
        fields = ['name', 'description', 'website', 'social_links']


class NnftForm(forms.ModelForm):
    error_css_class = 'error-field'
    required_css_class = 'required-field'
    #name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "NFT name"}))
    #description = forms.CharField(widget=forms.Textarea(attrs={"rows": 3}))
    class Meta:
        model = Nnft
        fields = ['collection', 'name', 'description', 'link_to_buy', 'attributes']
        widgets = {'collection': forms.HiddenInput()}


class NattributeForm(forms.ModelForm):
    class Meta:
        model = Nattribute
        fields = ['category', 'name']
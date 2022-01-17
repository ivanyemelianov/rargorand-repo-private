from django import forms


from .models import NftCollection

class NftCollectionForm(forms.ModelForm):
    class Meta:
        model = NftCollection
        fields = ['name', 'description']
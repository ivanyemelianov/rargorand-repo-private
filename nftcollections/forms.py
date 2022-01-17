from django import forms


from .models import NftCollection

class NftCollectionForm(forms.ModelFrom):
    class Meta:
        model = NftCollection
        fields = ['name', 'description']
from django import forms


from .models import NftCollection, Nft

class NftCollectionForm(forms.ModelForm):
    class Meta:
        model = NftCollection
        fields = ['name', 'description']

class NftForm(forms.ModelForm):
    class Meta:
        model = Nft
        fields = ['name', 'description']
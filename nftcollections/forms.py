from django import forms


from .models import NftCollection, Nft, NftImage

class NftImageForm(forms.ModelForm):
    class Meta:
        model = NftImage
        fields = ['image']

class NftCollectionForm(forms.ModelForm):
    error_css_class = 'error-filed'
    required_css_class = 'required-field'
    name = forms.CharField(help_text='This is your help! <a href="/contact">Contact us</a>')
    class Meta:
        model = NftCollection
        fields = ['name', 'description', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # django-crispy-forms
        for field in self.fields:
            new_data = {
                "placeholder": f'Collection {str(field)}',
                "class": 'form-control',
                #"hx-post": ".",
                #"hx-trigger": "keyup changed delay:500ms",
                #"hx-target": "#nftcollection-container",
                #"hx-swap": "outerHTML"
            }
            self.fields[str(field)].widget.attrs.update(
                new_data
            )
        # self.fields['name'].label = ''
        # self.fields['name'].widget.attrs.update({'class': 'form-control-2'})
        self.fields['description'].widget.attrs.update({'rows': '2'})


class NftForm(forms.ModelForm):
    class Meta:
        model = Nft
        fields = ['name', 'description', 'image']
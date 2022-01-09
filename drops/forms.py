from django import forms

from .models import Drop

class DropForm(forms.ModelForm):
    class Meta:
        model = Drop
        fields = ['title', 'description']

    def clean(self):
        data = self.cleaned_data
        title = data.get("title")
        qs = Drop.objects.filter(title__icontains=title)
        if qs.exists():
            self.add_error('title', 'This title is taken')
        return data
    
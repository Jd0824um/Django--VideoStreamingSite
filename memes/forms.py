from django import forms
from memes.models import Post


class MemeForm(forms.ModelForm):
    text = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Description of your meme...'
        }
    ))

    class Meta:
        model = Post
        fields = ('image','text',)

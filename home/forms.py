from django import forms
from home.models import Post


class HomeForm(forms.ModelForm):
    image = forms.ImageField()
    post = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Description of your meme...'
        }
    ))

    class Meta:
        model = Post
        fields = ('post',)

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Custom registration form
class Registration(UserCreationForm):
    email = forms.EmailField(required=True)

    # Defines the meta data of the Registration class
    class Meta:
        model = User
        fields = (
        'username',
        'first_name',
        'last_name',
        'email',
        'password1',
        'password2')

        def save(self, commit=True):
            user = super(Registration, self).save(commit=false)
            user.first_name = self.cleaned_data['first_name'] # Checks for any harmful strings
            user.last_name = self.cleaned_data['last_name']
            user.email = self.cleaned_data['email']

            if commit:
                user.save()

            return user

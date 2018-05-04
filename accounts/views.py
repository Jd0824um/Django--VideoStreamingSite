from django.shortcuts import render, redirect
from django.urls import reverse
from accounts.forms import (
    RegistrationForm,
    EditProfileForm,
)
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required


# Views homepage
def home(request):
    return render(request, 'accounts/home.html')

# Creates a new user from the register button
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:account').lstrip('/'))
    else:
        form = RegistrationForm()
        return render(request, 'accounts/registration.html', {'form' : form})

# Shows the user profile
def view_profile(request):
    return render(request, 'accounts/view_profile.html', {'user' : request.user})

# Allows editing of the user profile
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:profile').lstrip('/'))

    else:
        form = EditProfileForm(instance=request.user)
        return render(request, 'accounts/edit_profile.html', {'form' : form})

# Changes password for a user
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user) # Keeps user logged when the password has changed
            return redirect(reverse('accounts:profile').lstrip('/'))
        else:
            return redirect(reverse('accounts:change_password').lstrip('/')) # Loads the same form if the data is invalid

    else:
        form = PasswordChangeForm(user=request.user)
        return render(request, 'accounts/change_password.html', {'form' : form})

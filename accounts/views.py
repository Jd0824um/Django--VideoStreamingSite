from django.shortcuts import render, redirect
from accounts.forms import Registration


def home(request):
    return render(request, 'accounts/home.html')

# Creates a new user from the register button
def register(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account')
    else:
        form = Registration()
        return render(request, 'accounts/registration.html', {'form' : form})

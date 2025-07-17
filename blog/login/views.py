from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm

def login(request):

    return render(request, 'login.html', {'form': AuthenticationForm()})

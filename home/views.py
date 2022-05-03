from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login


# Create your views here.
def index(request):
    return render(request, 'index.html')


def loginUser(request):
    return render(request, 'login.html')


def logoutUser(request):
    return redirect('/login')


def contact(request):
    return render(request, 'contact.html')


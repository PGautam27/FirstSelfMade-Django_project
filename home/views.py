from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from home.models import Contact


# Create your views here.
def index(request):
    return render(request, 'index.html')


def loginUser(request):
    return render(request, 'login.html')


def logoutUser(request):
    return redirect('/login')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contacts = Contact(name, email, phone, desc)
        contacts.save()
    return render(request, 'contact.html')

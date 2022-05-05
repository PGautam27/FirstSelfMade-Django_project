from datetime import datetime

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from home.models import Contact


# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')


def loginUser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username, password)
        if user is not None:
            login(request, user)
            return redirect("/")
    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect('/login')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contacts = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contacts.save()
    return render(request, 'contact.html')

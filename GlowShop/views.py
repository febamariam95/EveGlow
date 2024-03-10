from django.shortcuts import render


# Create your views here.
from django.shortcuts import render

def About(request):
    return render(request, 'about.html')



def Contact(request):
    return render(request, 'contact.html')

def Index(request):
    return render(request, 'index.html')

def Login(request):
    return render(request, 'login.html')

def Products(request):
    return render(request, 'products.html')

def Register(request):
    return render(request, 'register.html')


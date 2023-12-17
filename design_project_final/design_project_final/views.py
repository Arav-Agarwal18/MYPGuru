from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import  render, redirect

def home_page(request):
    return render(request, "index.html")

def login_page(request):
    return render(request, "login.html")
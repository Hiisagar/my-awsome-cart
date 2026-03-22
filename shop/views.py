from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'shop/index.html')

def about(request):
    return HttpResponse("About page")

def contact(request):
    return HttpResponse("Contact page")

def tracker(request):
    return HttpResponse("Tracker page")

def search(request):
    return HttpResponse("Search page")

def productview(request):
    return HttpResponse("Product view page")

def checkout(request):
    return HttpResponse("Checkout page")
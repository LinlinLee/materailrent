from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def rent_index(request):
    return HttpResponse("Hello world.")

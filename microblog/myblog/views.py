from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse('<h1>Subham Das, did it!!!</h1>')

# Create your views here.
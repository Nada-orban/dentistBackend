
from django.shortcuts import render
from django.http import HttpResponse



def index(request):
  return HttpResponse('hello nada')

# Create your views here.

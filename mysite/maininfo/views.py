from django.http import HttpResponse
from django.shortcuts import render

def mainPage(request):
    return HttpResponse("WELCOME")

def detail(request, id):
    return HttpResponse('You\'re on page %s' %id)

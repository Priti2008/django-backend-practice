from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("Hello world. You are at the home page.")
    return render(request,'index.html')

def contact(request):
    return HttpResponse("for further query you can contact us")

def about(request):
    return HttpResponse("to know more about ourself")
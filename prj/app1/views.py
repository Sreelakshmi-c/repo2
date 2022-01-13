from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fnHome(request0):
    return HttpResponse("hi welcome to baabtra")
def fnIndex(request):
    return render(request,'index.html')

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    string = "<!DOCTYPE html><html><title>Things</title><h1>Things</h1></html>"
    return HttpResponse(string, content_type="text/html")

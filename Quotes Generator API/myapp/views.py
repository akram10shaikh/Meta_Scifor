from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    return render(request,'index.html')

def show(request):
    api = requests.get("https://api.quotable.io/random")
    quotes = api.json()
    return render(request,'index.html',{'quotes':quotes})


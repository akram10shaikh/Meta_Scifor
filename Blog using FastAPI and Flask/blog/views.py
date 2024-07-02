from django.shortcuts import render
import requests
# Create your views here.


def index(request):
    response = requests.get('http://127.0.0.1:8000/items')
    posts = response.json()
    return render(request,'index.html',{'posts':posts})
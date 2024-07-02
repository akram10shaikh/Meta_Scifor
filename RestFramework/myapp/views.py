from django.shortcuts import render
from rest_framework import generics
from .models import Category_Model,Post_Model
from .serializers import Category_serializer,Post_serializer

# Create your views here.
class Categorylist(generics.ListCreateAPIView):
    queryset = Category_Model.objects.all()
    serializer_class = Category_serializer

class Categorydetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category_Model.objects.all()
    serializer_class = Category_serializer


class Postlist(generics.ListCreateAPIView):
    queryset = Post_Model.objects.all()
    serializer_class = Post_serializer


class Postdetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post_Model.objects.all()
    serializer_class = Post_serializer


# Templates Views

def home(request):
    cat = Category_Model.objects.all()
    post = Post_Model.objects.all()
    return render(request,'index.html',{'cat':cat,'post':post})


from rest_framework import serializers
from .models import Category_Model,Post_Model

class Category_serializer(serializers.ModelSerializer):
    class Meta:
        model = Category_Model
        fields = '__all__'

class Post_serializer(serializers.ModelSerializer):
    class Meta:
        model = Post_Model
        fields = '__all__'
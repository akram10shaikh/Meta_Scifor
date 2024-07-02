from django.contrib import admin
from .models import Category_Model,Post_Model
# Register your models here.

admin.site.register(Category_Model)
admin.site.register(Post_Model)


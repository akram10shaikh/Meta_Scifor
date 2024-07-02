from django.urls import path
from .views import Categorylist,Categorydetail,Postlist,Postdetail
from . import views

urlpatterns = [
    path('category/',Categorylist.as_view()),
    path('category/<int:pk>/',Categorydetail.as_view()),
    path('post/',Postlist.as_view()),
    path('post/<int:pk>/',Postdetail.as_view()),

    path('',views.home,name='home'),
]
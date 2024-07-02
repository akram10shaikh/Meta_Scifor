
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('add_data/',views.add_data,name='add_data'),
    path('showdata/',views.showdata,name='showdata'),
    path('update_data/<str:_id>/',views.update_data,name='update_data'),
    path('edit/',views.edit,name='edit'),
]

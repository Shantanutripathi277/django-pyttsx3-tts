from cgitb import html
from django.contrib import admin
from django.urls import path
from transcript import views 
urlpatterns = [
    path ("", views.index , name="home"),
    # path ("work",views.get_name ,name="work")
]
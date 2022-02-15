from cgitb import html
from django.contrib import admin
from django.urls import path
from transcript import views 
urlpatterns = [
    path ("", views.index , name="home"),
    path("vid",views.upload_file,name="converter"),
    path('login/', views.signin),
    path('logout/', views.signout),
    path('signup/', views.signup),
    ]
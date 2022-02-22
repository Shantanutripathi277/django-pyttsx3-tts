from cgitb import html
from django.contrib import admin
from django.urls import path
from transcript import views 
urlpatterns = [
    path ("", views.signin , name="home"),
    #Directs to run the signin function of views script
    path ("index", views.index , name="home"),
    #Directs to run the views function of views script
    path("vid",views.upload_file,name="converter"),
    #Directs to run the upload_file function of views script
    path('login/', views.signin),
    #Directs to the run the signin function of views script
    path('logout/', views.signout),
    #Directs to the run the signout function of views script
    path('signup/', views.signup),
    #Directs to the run the signup function of views script
    ]
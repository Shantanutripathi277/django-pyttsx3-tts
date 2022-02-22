from tkinter import Y
from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import NameForm
from .forms import UploadFileForm
from .vidstrip import handle_uploaded_file
from .tts import tts
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm, UserRegistrationForm
from django.http import HttpResponse
from django.contrib.auth.models import User


# Create your views here.
# def index(request):

#     return render (request, "index.html")

        
def getsession(request):  
        sname = request.session['transcripts']  
        print(sname) 


def index(request):
    # if this is a POST request we need to process the form data
    src = False
    request.session['transcripts']= []
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            src = "static/speech.mp3"
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            transcript = form.data["transcript"]
            voicetype = form.data["voice"]
            tts(transcript, voicetype)
            request.session['transcripts']=request.session['transcripts']+[transcript]
            getsession(request)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'index.html', {'form': form, 'src': src, 'fileform': ''})


# Imaginary function to handle an uploaded file.

def upload_file(request):
    vidsrc = False
    if request.method == 'POST':
        fileform = UploadFileForm(request.POST, request.FILES)
        if fileform.is_valid():
            handle_uploaded_file(request.FILES['file'], fileform.data['title'])
            vidsrc = "static/"+(fileform.data['title']) + ".mp4"
    else:
        fileform = UploadFileForm()
    return render(request, 'index.html', {'fileform': fileform, 'form': '', 'vidsrc': vidsrc})


def signin(request):
    form = UserForm()
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(
            request,
            username=username,
            password=password
        )
        if user is None:
            return render(request, 'login.html', {'form': form,'invalid':"invalid"})
        login(request, user)
        request.session['name'] = username
        return redirect('/index')
    else:
        form = UserForm()
        return render(request, 'login.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('/login')

def signup(request):
    form=UserRegistrationForm()
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        newuser = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email
        )
        try:
            newuser.save()
            return redirect('/login')
        except:
           return render(request, 'signup.html', {'form': form,'invalid':"gonewrong"})
    else:
        form = UserRegistrationForm()
    return render(request, 'signup.html', {'form': form})

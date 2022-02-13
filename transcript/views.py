from tkinter import Y
from django.shortcuts import redirect, render , HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import NameForm
from .forms import UploadFileForm
from .vidstrip import handle_uploaded_file
from .tts import tts


# Create your views here.
# def index(request):
   
#     return render (request, "index.html")


def index(request):
    # if this is a POST request we need to process the form data
    src = False
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            
            src ="static/songname.mp3"
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            transcript = form.data["your_name"]
            voicetype = form.data["voice"]
            tts(transcript,voicetype)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'index.html', {'form': form, 'src': src, 'fileform':''})


# Imaginary function to handle an uploaded file.

def upload_file(request):
    vidsrc=False
    if request.method == 'POST':
        fileform = UploadFileForm(request.POST, request.FILES)
        if fileform.is_valid():
            handle_uploaded_file(request.FILES['file'])
            vidsrc='static/input_video.mp4'
    else:
        fileform = UploadFileForm()
    return render(request, 'index.html', {'fileform': fileform, 'form':'','vidsrc':vidsrc})
from django.shortcuts import render , HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import NameForm
from .tts import tts


# Create your views here.
# def index(request):
   
#     return render (request, "index.html")


def index(request):
    # if this is a POST request we need to process the form data
    src = "static/songname.mp3"
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            transcript = form.data["your_name"]
            voicetype = form.data["voice"]
            print(voicetype)
            tts(transcript,voicetype)
            print(form.data["your_name"])

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'index.html', {'form': form, 'src': src})

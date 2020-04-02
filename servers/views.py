from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Server
from .forms import ServerForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    servers = Server.objects.all()
    context = {
        "servers": servers,
    }
    return render(request, "servers.html", context)

@login_required(login_url='/login/')
def add_server(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ServerForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            #n = form.cleaned_data["display_name"]
            #request.user.server_set.create(display_name=n)
            #add owner a different way
            newServer = Server(
                display_name=form.cleaned_data["display_name"],
                owner=request.user
            )
            newServer.save()
            # redirect to a new URL:
            return HttpResponseRedirect('../')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ServerForm()
    return render(request, 'add_server.html', {'form': form})
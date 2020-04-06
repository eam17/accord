from django.shortcuts import render
from .models import Channel

# Create your views here.
def channels_index(request, pk):
    # Conditions for object to retrieve
    channels = Channel.objects.filter(server_id=pk)
    context = {
        "channels": channels,
    }
    return render(request, "channels.html", context)
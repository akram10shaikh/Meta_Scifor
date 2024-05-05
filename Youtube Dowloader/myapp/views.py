from django.shortcuts import render
from pytube import *
# Create your views here.

def youtube(request):
    if request.method == 'POST':
        link = request.POST.get('link')
        quality = request.POST.get('quality')
        video = YouTube(link)

        if quality == 'low':
            stream = video.streams.get_lowest_resolution()
        elif quality == 'high':
            stream = video.streams.get_highest_resolution()
        else:
            stream = video.streams.get_lowest_resolution()

        stream.download()

        return render(request, 'youtube.html')

    return render(request, 'youtube.html')

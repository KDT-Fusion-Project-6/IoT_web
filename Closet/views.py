from django.shortcuts import render
from django.views.generic import ListView, DetailView
from Closet.models import Album, Photo

class AlbumLV(ListView):
    model = Album
    # {{ object }}

class AlbumDV(DetailView):
    model = Album
    # {{ object_list }}

class PhotoDV(DetailView):
    model = Photo
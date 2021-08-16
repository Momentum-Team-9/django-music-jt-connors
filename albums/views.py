# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from .models import Albums, Tracks
from .forms import AlbumForm


def albums_add(request):
    if request.method == 'GET':
        form = AlbumForm()
    else:
        form = AlbumForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='albums')
    return render(request, "albums/albums_add.html", {'form': form})

def albums_delete(request, pk):
    albums = get_object_or_404(Albums, pk=pk)
    if request.method == 'POST':
        albums.delete()
        return redirect(to='albums')
    
    return render(request, "albums/albums_delete.html", {"albums": albums})

def albums_detail(request, pk):
    albums = get_object_or_404(Albums, pk=pk)
    return render(request, 'albums/albums_detail.html', {'albums': albums})

def albums_edit(request, pk):
    albums = get_object_or_404(Albums, pk=pk)
    if request.method =='GET':
        form = AlbumForm(instance=albums)
    else:
        form = AlbumForm(data=request.POST, instance=albums)
        if form.is_valid():
            form.save()
            return redirect(to='albums')
    return render(request, 'albums/albums_edit.html', {'form': form, 'albums': albums})


def albums_list(request):
    albums = Albums.objects.all()
    return render(request, 'albums/albums_list.html', {'album': albums})












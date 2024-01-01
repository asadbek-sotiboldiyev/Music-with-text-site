from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from music.models import Artist
from .functions import create_artist


def ArtistListView(request):
	artists=Artist.objects.all()
	context={
		'artists':artists
	}
	return render(request,'artist/artists_list.html',context)

def ArtistView(request,artist_id):
	artist=Artist.objects.get(id=artist_id)
	musics=artist.musics.all()
	context={
		'artist':artist,
		'musics':musics
	}
	return render(request,'artist/artist.html',context)

@login_required(login_url="/aut/login/")
def ArtistAddView(request):
	if not request.user.is_superuser:
		return render(request,'404.html')
	users=User.objects.all()
	context={'users':users}
	if request.method=='POST':
		new_artist=create_artist(request)
		return redirect('artist_page',artist_id=new_artist.id)
	return render(request,'artist/artist_add.html',context)

@login_required(login_url="/aut/login/")
def ArtistDelete(request,artist_id):
	if not request.user.is_superuser:
		return render(request,'404.html')
	artist=Artist.objects.get(id=artist_id)
	artist.delete()
	return redirect('artistlist_page')
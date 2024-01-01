from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.shortcuts import get_object_or_404
import os
from .models import *
from .functions import create_music

def HomeView(request):
	return render(request,'home.html')

def MusicListView(request):
	musics=Music.objects.all()
	return render(request,'music/music_list.html',{'musics':musics})

def MusicView(request,music_id):
	music=get_object_or_404(Music, id=music_id)
	music_type=music.get_type()
	context={
		'music':music,
		'type':music_type,
		'artists':music.artist.all()
	}
	with open(os.path.join(settings.MEDIA_ROOT,f'{music.text}'), 'r', encoding='utf-8') as file:
		text=file.read()
		text=text.replace("\n","<br>")
	context['text']=text
	
	return render(request,'music/music.html',context)

@login_required(login_url='/auth/login')
def MusicAddView(request):
	if not request.user.is_staff:
		return render(request,'403.html')
	artists=Artist.objects.all()
	context={
		'artists':artists
	}
	if request.method=='POST':
		new_music=create_music(request)
		return redirect('music_page',music_id=new_music.id)
	return render(request,'music/music_add.html',context)

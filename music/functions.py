from .models import Music,Artist

def create_music(request):
    title=request.POST.get('title')
    artists=request.POST.getlist('artist')
    new_music=Music.objects.create(
        title=title,
        music_img=request.FILES.get('music_img'),
        music=request.FILES.get('music'),
        text=request.FILES.get('text')
        )
    new_music.save()
    for artist_id in artists:
        artist=Artist.objects.get(id=int(artist_id))
        artist.musics.add(new_music)
        artist.save()
        new_music.artist.add(artist)
        new_music.save()
    return new_music

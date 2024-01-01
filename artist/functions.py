from music.models import Artist
from django.contrib.auth.models import User

def create_artist(request):
    name=request.POST['name']
    user=User.objects.get(id=int(request.POST['user']))
    profile_img=request.FILES.get('profile_img')
    new_artist=Artist.objects.create(name=name,user=user,profile_img=profile_img)
    new_artist.save()
    return new_artist
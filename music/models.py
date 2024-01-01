from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

class Artist(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	name=models.CharField(max_length=250)
	musics=models.ManyToManyField('Music',
		related_name='artist_musics')
	profile_img=models.ImageField(
		upload_to='artist-profile/',
		null=True,blank=True,
		default='artist-profile/default.jpg'
		)

	def __str__(self):
		return self.name

class Music(models.Model):
	title=models.CharField(max_length=250)
	artist=models.ManyToManyField('Artist',related_name='mus_artists')
	music=models.FileField(
		upload_to='musics_f/',
		unique=True,blank=True,null=True,
		validators=[FileExtensionValidator(['mp3','wav','ogg'])]
		)
	text=models.FileField(
		upload_to='texts/',
		blank=True,null=True,
		validators=[FileExtensionValidator(['txt'])]
		)
	music_img=models.ImageField(
		upload_to='music-profile/',
		null=True,blank=True,
		default='music-profile/default.jpg'
		)
	created_at=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

	def get_type(self):
		ext=str(self.music).split('.')[-1]
		return ext
	
	def artists_str(self):
		artists_lst=self.artist.all()
		lst=[str(i.name) for i in artists_lst]
		return ', '.join(lst)
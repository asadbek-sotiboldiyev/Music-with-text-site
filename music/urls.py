from django.urls import path
from .views import *

urlpatterns=[
	path('',HomeView,name='home_page'),
	path('musics/',MusicListView,name='musiclist_page'),
	path('music/add',MusicAddView,name='musicadd_page'),
	path('music/<int:music_id>',MusicView,name='music_page'),
]
from django.urls import path
from .views import *

urlpatterns=[
	path('artists/',ArtistListView,name="artistlist_page"),
	path('artist/add/',ArtistAddView,name="artistadd_page"),
	path('artist/<int:artist_id>',ArtistView,name="artist_page"),
	path('artist/<int:artist_id>/delete/',ArtistDelete,name="artistdelete_page"),
]
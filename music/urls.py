from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    url(r'^$', views.IndexView.as_view(), name='index'),

    #/music/music_id
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    #/music/album/add
    url(r'album/add/$', views.AlbumCreat.as_view(), name='album_add'),

    #/music/album/music_id
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album_update'),

    #/music/album/music_id/delete
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album_delete'),

   
]
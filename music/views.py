from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy 
from .models import Album

from django.shortcuts import render
from django.http import HttpResponse

#class base view 

class IndexView(generic.ListView):
	template_name = 'music/index.html'
	context_object_name='all_albums'
	
	

	def get_queryset(self):
		return Album.objects.all()
	
class DetailView(generic.DetailView):
	model = Album
	template_name = 'music/detail.html'

class AlbumCreat(CreateView):
	model = Album
	fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumUpdate(UpdateView):
	model = Album
	fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumDelete(DeleteView):
	model = Album
	success_url = reverse_lazy('music:index')


# function base view

def SearchAlbum(request):
	if request.method == "POST":
		saerch_text = request.POST['search_text']
	else:
		search_text = ''

	album_search = Album.objects.filter(title__contains=search_text)

	return render_to_response('music/search.html', {'album_search' : album_search})


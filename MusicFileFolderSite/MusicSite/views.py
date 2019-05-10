from django.shortcuts import render
from django.http import HttpResponse
# para trabajar templates en archivos diferentes
# Create your views here.
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Album, Song
from django.http import Http404



class IndexView(generic.ListView):
    template_name='MusicSite/index.html'
    context_object_name = 'all_albums'
    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name='MusicSite/detail.html'


# def index(request):
#     all_albums = Album.objects.all()
#     html = ''
#     # template = loader.get_template('MusicSite/index.html')
#     # django busca por defecto la carpeta template, por loque no hizo falta ponerlo
#     context = {
#         'all_albums': all_albums
#     }
#
#     ###for album in all_albums:
#     ###   url ='/music/' +str(album.id) +'/'
#     ###    html += '<a href="'+url+'">'+album.album_title+'</a><br>'
#     ##return HttpResponse("<h1>Esta es la pagina de musica</h1>")
#     ###return HttpResponse(html)
#     # return HttpResponse(template.render(context,request))
#     return render(request, 'MusicSite/index.html', context)
#
#
# def detail(request, album_id):  # esta funcioin es la que retorna la informacion
#     # de los albumes, realmente es un api lo que estamos
#     # creando creo
#     album = get_object_or_404(Album, pk=album_id, )
#     # try:
#     #     album = Album.objects.get(id=album_id)
#     # except  Album.DoesNotExist:
#     #     raise Http404('Este Album No existe: ID'+str(album_id))
#     return render(request, 'MusicSite/detail.html', {'album': album})
#
#
# def favorite(request, album_id):
#     album = get_object_or_404(Album, pk=album_id, )
#     try:
#         selected_song = album.song_set.get(pk=request.POST['song'])
#     except(KeyError, Song.DoesNotExist):
#         return render(request, 'MusicSite/detail.html', {
#             'album': album,
#             'error_message': 'No seleccionaste una cancion correcta',
#         })
#     else:
#         selected_song.is_favorite = not selected_song.is_favorite
#         selected_song.save()
#         return render(request, 'MusicSite/detail.html', {'album': album})

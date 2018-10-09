from django.conf.urls import url, include
from . import views

urlpatterns = [

    url(r'^$', views.index, name='musicsite'),
    # aqui se declara algum_id
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detalles'),
    # la forma de darle like y almacenarlo en nuestro sitio
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),

]
# esto es un cambio

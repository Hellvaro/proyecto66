from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from apps.appmusicoenvivo import views
from apps.appmusicoenvivo.views import registroUsuario
from django.contrib.auth.views import login
from django.conf import settings


urlpatterns = [
    # Examples:
    # url(r'^$', 'musicoenvivo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^$', views.index.as_view(), name="index"),
    url(r'^donaciones/', views.donaciones.as_view(), name="donaciones"),
    url(r'^servicios/', views.servicios.as_view(), name="servicios"),
    url(r'^crearbanda/', views.formularioBanda, name="formularioBanda"),
    url(r'^crearmusico/', views.formularioMusico, name="formularioMusico"),
    url(r'^crearlocal/', views.formularioLocal, name="formularioLocal"),
    url(r'^menuUsuario/', views.menuUsuario.as_view(), name="menuUsuario"),
    url(r'^registrar/', registroUsuario.as_view(), name="registrar"),
    url(r'^bandas', views.bandaList.as_view(),name='bandas'),
    url(r'^bandadetalle/(?P<id>\d+)/$', views.bandaDetalle, name='bandadetalle'),
    url(r'^musicodetalle/(?P<id>\d+)/$', views.musicoDetalle, name='musicodetalle'),
    url(r'^localdetalle/(?P<id>\d+)/$', views.localDetalle, name='localdetalle'),
    url(r'^locales', views.localList.as_view(),name='locales'),
    url(r'^musicos', views.musicoList.as_view(),name='musicos'),
    url(r'^perfilbanda/', views.bandasPerfil.as_view(),name='perfilbanda'),
    url(r'^perfilmusico/', views.perfilMusico.as_view(),name='perfilmusico'),
    url(r'^perfillocal/', views.perfilLocal.as_view(),name='perfillocal'),
    url(r'^registroexitoso/', views.registroExitoso,name='registroexitoso'),
    url(r'^succes/', views.perfilExitoso.as_view(),name='perfilexitoso'),
    url(r'^editarBanda/(?P<pk>\d+)/$', views.bandaUpdate.as_view(),name='editarBanda'),
    url(r'^editarMusico/(?P<pk>\d+)/$', views.musicoUpdate.as_view(),name='editarMusico'),
    url(r'^editarLocal/(?P<pk>\d+)/$', views.localUpdate.as_view(),name='editarLocal'),
    url(r'^editarUsuario/(?P<pk>\d+)/$', views.userUpdate.as_view(),name='editarusuario'),
    url(r'^eliminarBanda/(?P<pk>\d+)/$', views.bandaDelete.as_view(),name='eliminarBanda'),
    url(r'^eliminarMusico/(?P<pk>\d+)/$', views.musicoDelete.as_view(),name='eliminarMusico'),
    url(r'^eliminarLocal/(?P<pk>\d+)/$', views.localDelete.as_view(),name='eliminarLocal'),
    url(r'^contacto/', views.contacto,name='contacto'),
    url(r'^searchB/', views.searchB,name='searchB'),
    url(r'^searchM/', views.searchM,name='searchM'),
    url(r'^searchL/', views.searchL,name='searchL'),
    url(r'^busqueda/', views.busqueda,name='busqueda'),


]+ static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
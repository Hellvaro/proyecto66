from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from apps.appmusicoenvivo import views
from apps.appmusicoenvivo.views import registroUsuario
from django.contrib.auth.views import login, logout_then_login
from django.conf import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'musicoenvivo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', login, {'template_name': 'appmusicoenvivo/login.html'}, name='login'),
    #url(r'^logout/', views.logout, name='logout'),
    url(r'^logout1/', logout_then_login, name='logout1'),
    url(r'^', include('apps.appmusicoenvivo.urls')),
    url(r'^chaining/', include('smart_selects.urls')),

]

"""miprimersitio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from login.views import Register
#from aplicacion.views import publi_detalle
from login.views import register, Register
from aplicacion.views import publi_detalle
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^login/$', 'login.views.login_page', name='login'),
    url(r'^logout/$', 'login.views.logout_page', name='logout'),
    #url(r'^register/$', 'login.views.register', name='register'), 
    url(r'^register/$', Register.as_view(), name='register'),
    url(r'^$', 'login.views.homepage', name='homepage'),
    url(r'^publi_cat/(?P<publi_id>\d+)/$', 'aplicacion.views.publi_listar', name='publi_listar'),
    url(r'^publi_detalle/(?P<publi_id>\d+)/$', 'aplicacion.views.publi_detalle',name='publi_detalle'),
    url(r'^perfil_usuario/(?P<usu_id>\d+)/$', 'aplicacion.views.perfil_usuario',name='perfil_usuario'),
    url(r'^crear_publi/$', 'aplicacion.views.crear_publi', name='crear_publi'),
    url(r'^admin_usuario/$', 'aplicacion.views.admin_usuario', name='administrar_usuario'),
    url(r'^publi_creada/(?P<user_id>\d+)/$', 'aplicacion.views.publi_Creada', name='publi_creada'),
    url(r'^postularse/(?P<user_id>\d+)/(?P<publi_id>\d+)$', 'aplicacion.views.postularse', name='postularse'),
    url(r'^publi_postuladas/(?P<user_id>\d+)/$', 'aplicacion.views.publi_postuladas', name='publi_postuladas'),
    url(r'^guardar_publi/(?P<user_id>\d+)/$', 'aplicacion.views.guardar_publi', name='guardar_publi'),
    url(r'^buscar/$', 'aplicacion.views.buscar', name='buscar'),
    url(r'^enviar_mail_a/(?P<postu_id>\d+)/(?P<unMail>[^/]+)/$', 'aplicacion.views.enviar_mail_a', name='enviar_mail_a'),
    url(r'^enviar_mail_r/(?P<postu_id>\d+)/(?P<unMail>[^/]+)/$', 'aplicacion.views.enviar_mail_r', name='enviar_mail_r'),
    #url(r'^enviar_mail_r/(?P<unMail>[^/]+)/$', 'aplicacion.views.enviar_mail_r', name='enviar_mail_r'),
    #url(r'^enviar_mail/$', 'aplicacion.views.enviar_mail', name='enviar_mail')

]
from django.http import HttpResponse, Http404
from aplicacion.models import Publicacion, Usuario
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from aplicacion.forms import PublicacionForm

@login_required
def publi_detalle(request, publi_id):
	publi = Publicacion.objects.get(id=publi_id)
	return render_to_response('publi_detalle.html',	{'publi':publi}, 
		context_instance=RequestContext(request))

@login_required
def publi_listar(request, publi_id):
	publis = Publicacion.objects.filter(categoria_id=publi_id)
	return render_to_response('publi_listar.html', {'publis':publis}, 
		context_instance=RequestContext(request))

@login_required
def perfil_usuario(request, usu_id):
	usuario = Usuario.objects.get(id=usu_id)
	return render_to_response('perfil_usuario.html', {'usuario':usuario},
		context_instance=RequestContext(request))

@login_required
def crear_publi(request):
	form = PublicacionForm()
	return render_to_response('crear_publi.html', {'form':form},
		context_instance=RequestContext(request))
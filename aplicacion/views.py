from django.http import HttpResponse, Http404
from aplicacion.models import Publicacion, Usuario, Postulante
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from aplicacion.forms import PublicacionForm
import datetime

@login_required
def publi_detalle(request, publi_id):
	publi = Publicacion.objects.get(id=publi_id)
	postulacion = Postulante.objects.filter(publicacion_id = publi_id)
	resguardo = list()
	for p in postulacion:
		resguardo.append(p.usuario_id)
	return render_to_response('publi_detalle.html',	{'publi':publi,'resguardo':resguardo, 'postulacion':postulacion},
		context_instance=RequestContext(request))

@login_required
def publi_listar(request, publi_id):
	publis = Publicacion.objects.filter(categoria_id=publi_id)
	return render_to_response('publi_listar.html', {'publis':publis}, 
		context_instance=RequestContext(request))

@login_required
def perfil_usuario(request, usu_id):
	usuario = Usuario.objects.get(user_id=usu_id)
	return render_to_response('perfil_usuario.html', {'usuario':usuario},
		context_instance=RequestContext(request))

@login_required
def crear_publi(request):
	form = PublicacionForm()
	return render_to_response('crear_publi.html', {'form':form},
		context_instance=RequestContext(request))

@login_required
def admin_usuario(request):
	return render_to_response('admin_usuario.html',
		context_instance=RequestContext(request))

@login_required
def publi_Creada(request,user_id):
	publis = Publicacion.objects.filter(usuario=user_id)
	
	return render_to_response('publi_listar.html', {'publis':publis}, 
		context_instance=RequestContext(request))

@login_required
def buscar(request):
	valor = str(request.get['buscar'])
	publis = Publicacion.objects.filter(nombre__contains=request.get['buscar'])
	return render_to_response('publi_listar.html',{'publis':publis},
		context_instance=RequestContext(request))

@login_required
def postularse(request,user_id,publi_id):
	p = Postulante(usuario_id=user_id,publicacion_id=publi_id)
	p.save()
	return render_to_response('homepage.html',
		context_instance=RequestContext(request))

@login_required
def publi_postuladas(request,user_id):
	postulaciones = Postulante.objects.filter(usuario_id=user_id)
	publis = list()
	for postulacion in postulaciones:
		valor = int(postulacion.publicacion_id)
		publi = Publicacion.objects.get( id = valor)
		if (publi != None):
			publis.append(publi)
	return render_to_response('publi_listar.html', {'publis':publis},
		context_instance=RequestContext(request))

@login_required
def guardar_publi(request,user_id):
	x = datetime.datetime.now()
	cierre = request.GET['fecha_cierre_year'] + "-" + request.GET['fecha_cierre_month']+ "-"+request.GET['fecha_cierre_day']
	inicio = str(x.year) + "-" + str(x.month) + "-" + str(x.day)
	publi = Publicacion(nombre = request.GET['titulo'],
		fechaInicio = inicio ,
		fechaCierre = cierre ,
		cantidad = request.GET['integrantes'],
		descripcion = request.GET['descripcion'],
		usuario_id = user_id,
		categoria_id = request.GET['categoria'])
	publi.save()

	return render_to_response('homepage.html', 
		context_instance=RequestContext(request))
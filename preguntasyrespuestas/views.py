from django.http import HttpResponse, Http404
from preguntasyrespuestas.models import Pregunta
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from preguntasyrespuestas.forms import PreguntaForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def index(request):
	preguntas = Pregunta.objects.all()
	return render_to_response('preguntasyrespuestas/index.html', 
		{'preguntas':preguntas})

def pregunta_detalle(request, pregunta_id):
	pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
	return render_to_response('preguntasyrespuestas/pregunta_detalle.html',
		{'pregunta':pregunta})

@login_required
def pregunta_crear(request):
	if request.method == 'POST':
		form = PreguntaForm(request.POST)
		if form.is_valid():
			""" al usar ModelForm evito esta parte
			pregunta = Pregunta(asunto=form.cleaned_data['asunto'],
				descripcion=form.cleaned_data['descripcion'],
				fecha_publicacion=timezone.now())
			pregunta.save()
			"""
			form.save()
			return redirect('preguntas')
	else:
		form = PreguntaForm()
	return render_to_response('preguntasyrespuestas/pregunta_crear.html',
		{'form':form}, context_instance=RequestContext(request))

@login_required
def pregunta_editar(request, pregunta_id):
	pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
	if request.method == 'POST':
		form = PreguntaForm(request.POST, instance=pregunta)
		if form.is_valid():
			form.save()
			return redirect('pregunta_detalle', pregunta_id)
	else:
		form = PreguntaForm(instance=pregunta)
	return render_to_response('preguntasyrespuestas/pregunta_editar.html',
			{'form':form}, context_instance=RequestContext(request))

"""
def index_1(request):#devuelve html puro
	preguntas = Pregunta.objects.all()
	respuesta_string = "Preguntas <br/>"
	respuesta_string += '<br/>'.join(["id: %s, asunto: %s"%
	(p.id, p.asunto) for p in preguntas])
	return HttpResponse(respuesta_string)

def pregunta_detalle_1(request, pregunta_id):#sin uno de shortcuts
	try:
		pregunta = Pregunta.objects.get(pk=pregunta_id)
	except Pregunta.DoesNotExist:
		raise Http404
	return HttpResponse("%s?" % pregunta.asunto)

def pregunta_detalle_2(request, pregunta_id):#con uso de shortcuts
	pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
	return HttpResponse("%s?" % pregunta.asunto)
"""

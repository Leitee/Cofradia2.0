from django.http import HttpResponse, Http404
from aplicacion.models import Publicacion
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from django.utils import timezone
from django.contrib.auth.decorators import login_required

@login_required
def publi_detalle(request, publi_id):
	publi = Publicacion.objects.filter(categoria_id=publi_id)
	return render_to_response('publi_detalle.html',
		{'publis':publi}, context_instance=RequestContext(request))
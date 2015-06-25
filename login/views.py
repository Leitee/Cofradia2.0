from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from login.forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout

def login_page(request):
	message = None
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					message = "Te has identificado correctamente"
					return redirect('homepage')
				else:
					message = "Tu usuario esta inactivo"
			else:
				message = "Nombre de usuario y/o password incorrecto"
	else:
		form = LoginForm()
	return render_to_response('login.html', {'message':message, 'form': form},
		context_instance=RequestContext(request))

def homepage(request):
	return render_to_response('homepage.html',
		context_instance=RequestContext(request))

def logout_page(request):
	logout(request)
	return redirect('homepage')

def register(request):	
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		data = request.POST.copy()
		if form.is_valid():
			new_user = form.save(data)
			logoid(new_user)
			return redirect('homepage')
	else:
		form = RegisterForm()
	return render_to_response('register.html', 
		{'form' : form},
		context_instance=RequestContext(request))
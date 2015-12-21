from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse 
from django.shortcuts import redirect

# Create your views here.

def login_user(request):
	args={}
	if request.POST:
		username = request.POST.get('username','')
		password = request.POST.get('password','')
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				args['username'] = username
				return HttpResponseRedirect("/home/")
		else:
			args['username'] = username
			return render(request,'login.html',args)

	elif request.user.is_authenticated and request.user.is_active:
		return HttpResponseRedirect("/home/")
	else:
		return render(request,'login.html',args)

@login_required
def logout_user(request):
	logout(request)
	#request.session.clear()
	return HttpResponseRedirect("/")

@login_required(login_url='/')
def home(request):
	args={}
	args['username'] = request.user
	return render(request,'home.html',args)


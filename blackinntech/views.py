from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy

def index(request):
	return redirect('login')

def is_crm(user):
    return user.groups.filter(name='operador').exists() or user.groups.filter(name='comercial').exists()

def is_admin(user):
    return user.groups.filter(name='administrador').exists()

def logged_in(request):
    print 'loggin'
    if is_crm (request.user):
        print 'Crm user'
        return redirect('crm:index')
    if is_admin (request.user):
        print 'Administrador user'
        return redirect('admin:index')

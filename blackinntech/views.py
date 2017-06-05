from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy


def index(request):
	return redirect('login')


def is_oper(user):
    return user.groups.filter(name='operador').exists()

def is_admin(user):
    return user.groups.filter(name='administrador').exists()

def logged_in(request):
    print 'loggin'
    if is_oper (request.user):
        print 'operador'
        return redirect('crm:index')
    if is_admin (request.user):
        print 'Administrador'
        return redirect('admin:index')

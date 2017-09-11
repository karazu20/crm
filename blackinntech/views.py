from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy

def index(request):
	return redirect('login')

def is_crm(user):
    return user.groups.filter(name='admin').exists() or user.groups.filter(name='oper').exists()

def is_sys(user):
    return user.groups.filter(name='sys').exists()

def logged_in(request):
    print 'loggin'
    if is_crm (request.user):
        print 'is_crm user'
        return redirect('crm:index')
    if is_sys (request.user):
        print 'is_sys user'
        return redirect('admin:index')

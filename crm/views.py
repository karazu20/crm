# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from crm.models import *
from crm.forms import *
from django.core.urlresolvers import reverse_lazy
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.

LEAD_BAJA = 7
LEAD_ARRANQUE = 6
GRUPO_USER_COMERCIAL = 3

@login_required
def index(request):
	return render(request, 'crm/index.html')

##Ejecutivos##

class EjecutivoList(ListView):
	model = EjecutivoComercial
	template_name='crm/ejecutivo/list.html'

class EjecutivoCreate(CreateView):
	model = EjecutivoComercial
	form_class = EjecutivoForm
	template_name = 'crm/ejecutivo/add.html'
	success_url = reverse_lazy('crm:lista_ejecutivo')

@login_required
def ejecutivo_create(request):
	if request.method == 'POST':
		formEjecutivo = EjecutivoForm(request.POST)
		formUser = UserCreateForm(request.POST)
		if formUser.is_valid() &  formEjecutivo.is_valid():
			user=formUser.save()
			user.email=request.POST['mail']
			user.groups.add(GRUPO_USER_COMERCIAL)
			user.first_name=request.POST['nombre']
			user.save()
			ejecutivo = formEjecutivo.save()
			ejecutivo.user = user
			ejecutivo.save()
			return redirect('crm:lista_ejecutivo')
		else:
			print 'datos invalidos'
			return render(request, 'crm/ejecutivo/add.html', {'form': formEjecutivo,  'formUser': formUser})
	else:
		formEjecutivo = EjecutivoForm()
		formUser = UserCreateForm()
		return render(request, 'crm/ejecutivo/add.html', {'form': formEjecutivo, 'formUser': formUser })


class EjecutivoUpdate(UpdateView):
	model = EjecutivoComercial
	form_class = EjecutivoForm
	template_name = 'crm/ejecutivo/update.html'
	success_url = reverse_lazy('crm:lista_ejecutivo')

class EjecutivoDelete(DeleteView):
	model = EjecutivoComercial
	template_name = 'crm/generic_form_delete.html'
	success_url = reverse_lazy('crm:lista_ejecutivo')

##Empresas##
class EmpresaList(ListView):
	model = Empresa
	template_name = 'crm/empresa/list.html'

class EmpresaCreate(CreateView):
	model = Empresa
	form_class = EmpresaForm
	template_name = 'crm/empresa/add.html'
	success_url = reverse_lazy('crm:lista_empresa')

class EmpresaUpdate(UpdateView):
	model = Empresa
	form_class = EmpresaForm
	template_name = 'crm/empresa/update.html'
	success_url = reverse_lazy('crm:lista_empresa')

class EmpresaDelete(DeleteView):
	model = Empresa
	template_name = 'crm/generic_form_delete.html'
	success_url = reverse_lazy('crm:lista_empresa')

##Contactos##
class ContactoList(ListView):
	model = Contacto
	template_name = 'crm/contacto/list.html'


class ContactoCreate(CreateView):
	model = Contacto
	form_class = ContactoForm
	template_name = 'crm/contacto/add.html'
	success_url = reverse_lazy('crm:lista_contacto')

class ContactoUpdate(UpdateView):
	model = Contacto
	form_class = ContactoForm
	template_name = 'crm/contacto/update.html'
	success_url = reverse_lazy('crm:lista_contacto')

class ContactoDelete(DeleteView):
	model = Contacto
	template_name = 'crm/generic_form_delete.html'
	success_url = reverse_lazy('crm:lista_contacto')

##Leads##


def is_oper(user):
	return user.groups.filter(name='operador').exists()

def is_comer(user):
	return user.groups.filter(name='comercial').exists()

class LeadList(ListView):
	model = LeadDetalle
	template_name = 'crm/lead_list.html'

	def get_queryset(self):
		print self.request.user.id
		if is_oper(self.request.user):
			queryset = LeadDetalle.objects.filter(es_vigente=True, lead__owner=self.request.user)
		else:
			queryset = LeadDetalle.objects.filter(Q(es_vigente=True) &
				(Q(ejecutivo_principal__user=self.request.user) |
				 Q(ejecutivo_primario__user=self.request.user) |
				 Q(ejecutivo_secundario__user=self.request.user)))
		return queryset


class LeadCreate(CreateView):
	model = LeadDetalle
	form_class = LeadDetalleForm
	template_name = 'crm/generic_form.html'
	success_url = reverse_lazy('crm:lista_lead')

def prev_comments(lead):
	detalles = LeadDetalle.objects.filter(lead_id=lead.id).order_by('id')
	comments = dict()
	for d in detalles:
		print d.etapa_id
		comments[d.etapa.id] = d.comentarios
	return comments

@login_required
def lead_create(request):
	if request.method == 'POST':
		form = LeadDetalleForm(request.POST)
		print 'in post'
		if form.is_valid():
			leadDetalle = form.save()
			lead =  Lead()
			lead.fecha_lnc = datetime.now()
			lead.owner=request.user
			lead.save()
			leadDetalle.lead = lead
			print 'save lead ' + str(lead.id)
			etapa=EtapasLeads.objects.get(id=1)
			leadDetalle.etapa=etapa
			leadDetalle.save()
			print 'save leadDetalle ' + str (leadDetalle.id)
			return redirect('crm:lista_lead')
		else:
			print 'datos invalidos'
			return render(request, 'crm/lead/add.html', {'form':form})
	else:
		form = LeadDetalleForm()
		return render(request, 'crm/lead/add.html', {'form':form})


@login_required
def lead_baja(request, id):
	print 'baja de ' +str (id)
	detalle = LeadDetalle.objects.get(id=id)
	if not detalle.es_vigente:
		return redirect('crm:lista_lead')
	if request.method == 'POST':
		form = LeadDetalleForm(request.POST)
		if form.is_valid():
			lead = Lead.objects.get(id=detalle.lead_id)
			detalle.es_vigente = False
			detalle.save()
			#S e da de baja el lead
			etapaBaja = EtapasLeads.objects.get(id=LEAD_BAJA)
			detalle_baja = form.instance
			detalle_baja.etapa = etapaBaja
			detalle_baja.id = None
			detalle_baja.lead = lead
			detalle_baja.es_vigente = True
			detalle_baja.save()
			# add productos
			productos = form.cleaned_data['producto']
			detalle_baja.producto = productos
			detalle_baja.save()
			lead.fecha_baja = datetime.now()
			lead.save()
			print 'termina baja'
			return redirect('crm:lista_lead')
		else:
			print 'datos invalidos'
			return render(request, 'crm/lead_form_delete.html', {'form': form, 'lead_detalle': detalle})
	else:
		print 'get'
		form = LeadDetalleForm(instance=detalle)
		return render(request, 'crm/lead_form_delete.html', {'form': form, 'lead_detalle': detalle})

@login_required
def lead_init(request, id):
	print 'init de ' + str(id)
	detalle = LeadDetalle.objects.get(id=id)
	if not detalle.es_vigente:
		return redirect('crm:lista_lead')
	if request.method == 'POST':
		form = LeadDetalleForm(request.POST)
		if form.is_valid():
			lead = Lead.objects.get(id=detalle.lead_id)
			#Se da quita como vigente el lead actual
			detalle.es_vigente = False
			detalle.save()
			#Se guada fecha real de Lead
			fecha = con_factura = request.POST['date']
			fecha_real_init = datetime.strptime(fecha, '%Y/%M/%d')
			lead.fecha_real_init = fecha_real_init
			lead.save()
			# S e da de baja el lead
			new_etapa = EtapasLeads.objects.get(id=LEAD_ARRANQUE)
			detalle_init = form.instance
			detalle_init.etapa = new_etapa
			detalle_init.id = None
			detalle_init.lead = lead
			detalle_init.es_vigente = True
			detalle_init.save()
			# add productos
			productos = form.cleaned_data['producto']
			detalle_init.producto = productos
			detalle_init.save()

			print 'termina arranque'
			return redirect('crm:lista_lead')
		else:
			print 'datos invalidos'
			return render(request, 'crm/lead_form_init.html', {'form': form, 'lead_detalle': detalle})
	else:
		print 'get'
		form = LeadDetalleForm(instance=detalle)
		return render(request, 'crm/lead_form_init.html', {'form': form, 'lead_detalle': detalle})

@login_required
def lead_next(request, id):
	detalle = LeadDetalle.objects.get(id=id)
	lead = Lead.objects.get(id=detalle.lead_id)
	if not detalle.es_vigente:
		return redirect('crm:lista_lead')
	if request.method == 'POST':

		form = LeadDetalleForm(request.POST)
		if form.is_valid():
			# Se obtiene el lead y se actualiza
			etapa = detalle.etapa
			print (etapa.nombre)
			new_etapa = EtapasLeads.objects.get(id=(etapa.id+1))
			if new_etapa.id  == 2 : #LC
				lead.fecha_lc = datetime.now()
			elif new_etapa.id  == 3: #OP
				lead.fecha_op = datetime.now()
			elif  new_etapa.id == 4: #NEG
				lead.fecha_neg = datetime.now()
			else:  #CIE
				lead.fecha_cie = datetime.now()
				fecha = request.POST['date']
				#print fecha_plan_init
				fecha_plan_init = datetime.strptime(fecha, '%Y/%M/%d')
				lead.fecha_plan_init=fecha_plan_init
			lead.save()
			#Se clona el detalle"
			detalle_new = form.instance
			detalle_new.etapa = new_etapa
			detalle_new.id = None
			detalle_new.lead = lead
			#for p in detalle_new.producto.all():
			#	print p.nombre
			detalle_new.save()
			# se quita como vigente el detalle anterior
			detalle.es_vigente=False
			detalle.save()
			#add productos
			productos = form.cleaned_data['producto']
			detalle_new.producto = productos
			detalle_new.save()
			return redirect('crm:lista_lead')
		else:
			print 'datos invalidos'
			return render(request, 'crm/lead_form_next.html', {'form': form})
	else:
		#detalle.producto = Producto.objects.get(producto_lead=detalle)
		form = LeadDetalleForm(instance=detalle)
		for p in detalle.producto.all():
			print p.nombre
		today = timezone.now()
		print today
		print lead.fecha_lnc

		time_life = abs((today - lead.fecha_lnc).days)
		comments = prev_comments(lead)
		return render(request, 'crm/lead_form_next.html', {'form':form, 'lead_detalle':detalle, 'time_life':time_life, 'comments':sorted(comments.items(),reverse=True)})


@login_required
def lead_details(request, id):
	print 'deatalles de ' +str (id)
	detalle = LeadDetalle.objects.get(id=id)
	lead = Lead.objects.get(id=detalle.lead_id)
	listLeads = LeadDetalle.objects.filter(lead=lead)
	if not detalle.es_vigente:
		return redirect('crm:lista_lead')
	print 'get'
	return render(request, 'crm/lead_details.html', {'object_list': listLeads})


class LeadUpdate(UpdateView):
	model = LeadDetalle
	form_class = LeadDetalleForm
	template_name = 'crm/generic_form.html'
	success_url = reverse_lazy('crm:lista_lead')

class LeadDelete(DeleteView):
	model = LeadDetalle
	template_name = 'crm/generic_form_delete.html'
	success_url = reverse_lazy('crm:lista_lead')

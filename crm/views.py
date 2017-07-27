# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from crm.models import *
from crm.forms import *
from crm import gmail
from django.core.urlresolvers import reverse_lazy
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.db.models import Q
#from django.conf import settings
from hashids import Hashids
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
"""Varible para generar los tokens 
para la creación de las cuentas de los usuarios"""
hashids = Hashids(salt="CrmP4$$w0rd2017",min_length=16)

'Constantes para validaciones'
LEAD_BAJA = 7
LEAD_ARRANQUE = 6
GRUPO_USER_OPERATIVO = 3

"""Direcciona al index que sta definido 
como la pagina del login"""
@login_required
def index(request):
	return render(request, 'crm/index.html')

##User##
"""Se crea el usuario apartir del token 
generado para el ejecutivo"""
def create_user(request, folio):
	print 'in user create'
	id = hashids.decode(folio)
	print str (id)
	if request.method == 'POST':
		form = UserCreateForm(request.POST)
		ejecutivo = EjecutivoComercial.objects.get(id=int(id[0]))
		print 'id ejecutivo: ' + str (id)
		print 'Se crea usuario'
		if form.is_valid():
			user = form.save()
			user.email = ejecutivo.mail
			user.groups.add(ejecutivo.perfil)
			user.first_name = ejecutivo.nombre
			user.save()
			ejecutivo.user=user
			ejecutivo.save()
			user = authenticate(request, username=request.POST['username'], password=request.POST['password1'])
			login(request, user)
			return redirect('crm:index')
		else:
			print 'datos invalidos'
			return render(request, 'crm/user/add.html', {'form': form})
	else:
		if len(id) > 0:
			form = UserCreateForm()
			return render(request, 'crm/user/add.html', {'form':  form})

		else:
			raise Http404("No se encontró la pagina contacte a su administrador o pida que se genere de nuevo la solicitud de usuario CRM")


##Ejecutivos##
"""Lanza la lista de los ejecutivos 
se ordenan por nombre"""
class EjecutivoList(ListView):
	model = EjecutivoComercial
	queryset = EjecutivoComercial.objects.order_by('nombre')
	template_name='crm/ejecutivo/list.html'

"""Se crea un ejecutivo y
redirecciona a la lista de ejecutivos"""
class EjecutivoCreate(CreateView):
	model = EjecutivoComercial
	form_class = EjecutivoForm
	template_name = 'crm/ejecutivo/add.html'
	success_url = reverse_lazy('crm:lista_ejecutivo')

	"""Se genera un toker para la generación 
	de la cuenta del usuario y se manda por correo"""
	def form_valid(self, form):
		name = self.request.POST['nombre']
		mail = self.request.POST['mail']
		ejecutivo=form.save()
		folio = hashids.encode(ejecutivo.id)
		url= 'http://' + self.request.get_host() + '/crm/user/add/' + str (folio)
		gmail.sendMail(mail, name, url)
		return redirect('crm:lista_ejecutivo')

"""Se crea el ejucutivo con todo y usuario
metodo deprecated"""
@login_required
def ejecutivo_create(request):
	if request.method == 'POST':
		formEjecutivo = EjecutivoForm(request.POST)
		formUser = UserCreateForm(request.POST)
		if formUser.is_valid() &  formEjecutivo.is_valid():
			user=formUser.save()
			user.email=request.POST['mail']
			user.groups.add(GRUPO_USER_OPERATIVO)
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

"""Se actualiza el ejecutivo y 
se direcciona  a la lista de ejecutivos"""
class EjecutivoUpdate(UpdateView):
	model = EjecutivoComercial
	form_class = EjecutivoForm
	template_name = 'crm/ejecutivo/update.html'
	success_url = reverse_lazy('crm:lista_ejecutivo')

"""Se borra el ejecutivo y se direcciona
a la lista de ejecutivos"""
class EjecutivoDelete(DeleteView):
	model = EjecutivoComercial
	template_name = 'crm/generic_form_delete.html'
	success_url = reverse_lazy('crm:lista_ejecutivo')

##Empresas##
"""Lanza la lista de las empresas 
se ordenan por nombre"""
class EmpresaList(ListView):
	model = Empresa
	queryset = Empresa.objects.order_by('nombre')
	template_name = 'crm/empresa/list.html'

"""Se crea una empresa y
redirecciona a la lista de empresas"""
class EmpresaCreate(CreateView):
	model = Empresa
	form_class = EmpresaForm
	template_name = 'crm/empresa/add.html'
	success_url = reverse_lazy('crm:lista_empresa')

"""Se actualiza la empresa y 
se direcciona  a la lista de empresas"""
class EmpresaUpdate(UpdateView):
	model = Empresa
	form_class = EmpresaForm
	template_name = 'crm/empresa/update.html'
	success_url = reverse_lazy('crm:lista_empresa')

"""Se borra la empresa y se direcciona
a la lista de empresas"""
class EmpresaDelete(DeleteView):
	model = Empresa
	template_name = 'crm/generic_form_delete.html'
	success_url = reverse_lazy('crm:lista_empresa')

##Contactos##
"""Lanza la lista de los contactos 
se ordenan por nombre"""
class ContactoList(ListView):
	model = Contacto
	queryset = Contacto.objects.order_by('nombre')
	template_name = 'crm/contacto/list.html'

"""Se crea un contacto y
redirecciona a la lista de contactos"""
class ContactoCreate(CreateView):
	model = Contacto
	form_class = ContactoForm
	template_name = 'crm/contacto/add.html'
	success_url = reverse_lazy('crm:lista_contacto')

"""Se actualiza el contacto y 
se direcciona  a la lista de contactos"""
class ContactoUpdate(UpdateView):
	model = Contacto
	form_class = ContactoForm
	template_name = 'crm/contacto/update.html'
	success_url = reverse_lazy('crm:lista_contacto')

"""Se borra el contacto y se direcciona
a la lista de contactos"""
class ContactoDelete(DeleteView):
	model = Contacto
	template_name = 'crm/generic_form_delete.html'
	success_url = reverse_lazy('crm:lista_contacto')

##Leads##
'Valida si el usuario es admin'
def is_admin(user):
	return user.groups.filter(name='admin').exists()
'Valida si el usuario es oper'
def is_oper(user):
	return user.groups.filter(name='oper').exists()

"""Genera los folios de los leads se actualizan, 
deprecated sólo si se necesita que se actualizen"""
def generateFolios(detalles):
	cont = 0
	for detalle in detalles:
		lead = Lead.objects.get(id=detalle.lead_id)
		cont = cont + 1
		lead.folio = cont
		lead.save()

"""Lista los lead, los ordena por folio y
muestra de acuerdo al rol del usuario"""
class LeadList(ListView):
	model = LeadDetalle
	template_name = 'crm/lead_list.html'

	def get_queryset(self):
		print self.request.user.id
		if is_admin(self.request.user):
			queryset = LeadDetalle.objects.filter(es_vigente=True ).order_by('lead__folio')
			generateFolios(queryset)
		else:
			queryset = LeadDetalle.objects.filter(Q(es_vigente=True) &
				(Q(ejecutivo_principal__user=self.request.user) |
				 Q(ejecutivo_primario__user=self.request.user) |
				 Q(ejecutivo_secundario__user=self.request.user))).order_by('lead__folio')
		return queryset

'Deprecated'
class LeadCreate(CreateView):
	model = LeadDetalle
	form_class = LeadDetalleForm
	template_name = 'crm/generic_form.html'
	success_url = reverse_lazy('crm:lista_lead')

'Obtiene los comentarios de un lead'
def prev_comments(lead):
	detalles = LeadDetalle.objects.filter(lead_id=lead.id).order_by('id')
	comments = dict()
	for d in detalles:
		print d.etapa_id
		comments[d.etapa.id] = d.comentarios
	return comments

'Genera el folio de un lead'
def generaFolio(lead):
	top = Lead.objects.order_by('-folio')[0]
	lead.folio = top.folio + 1

"""Se encarga de crear el Lead, con toda
su estructura inicial"""
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
			generaFolio(lead)
			#lead.folio=leadDetalle.empresa.nombre[:4] + '_' + str(leadDetalle.empresa.id) + '_' + str(lead.id)
			lead.save()
			print 'save leadDetalle ' + str (leadDetalle.id)
			return redirect('crm:lista_lead')
		else:
			print 'datos invalidos'
			return render(request, 'crm/lead/add.html', {'form':form})
	else:
		form = LeadDetalleForm()
		return render(request, 'crm/lead/add.html', {'form':form})

'Obtiene un attach de un lead'
@login_required
def get_attach (request, id):
	try:
		attahcment = Attachment.objects.get(id=id)
		doc = attahcment.doc
		print ('archivo: ' + doc.name)
		doc.open(mode='rb')
		response = HttpResponse(doc.read(), content_type='application/force-download')
		response['Content-Disposition'] = 'inline; filename="'+ doc.name +'"'
		return response
		doc.closed()
	except Exception, e:
		print e.message
		return HttpResponseNotFound('<h1>Doc not found</h1>')

'Obtiene un attach del checklist de un lead'
@login_required
def get_attach_check (request, id, campo):
	try:
		if campo=='rfc':
			comercial = InfoComercial.objects.get(id=id)
			doc=comercial.rfc
		elif campo=='acta':
			comercial = InfoComercial.objects.get(id=id)
			doc = comercial.acta
		elif campo == 'id':
			comercial = InfoComercial.objects.get(id=id)
			doc = comercial.id_apoderado
		else:
			finanzas = InfoFinanzas.objects.get(id=id)
			doc = finanzas.proceso_fact
		print ('archivo: ' + doc.name)
		doc.open(mode='rb')
		response = HttpResponse(doc.read(), content_type='application/force-download')
		response['Content-Disposition'] = 'inline; filename="'+ doc.name +'"'
		return response
		doc.closed()
	except Exception, e:
		print e.message
		return HttpResponseNotFound('<h1>Doc not found</h1>')

'Le crea un attach al lead'
@login_required
def lead_attach(request, id):
	detalle = LeadDetalle.objects.get(id=id)
	if not detalle.es_vigente:
		return redirect('crm:lista_lead')
	if request.method == 'POST':
		form = AttachmentForm(request.POST, request.FILES)
		if form.is_valid():
			lead = Lead.objects.get(id=detalle.lead_id)
			doc = form.save()
			doc.lead = lead
			doc.save()
			return redirect('crm:lista_lead')
		else:
			return render(request, 'crm/lead_attachment.html', {'form': form, 'lead_detalle': detalle})
	else:
		print 'get'
		form = AttachmentForm()
		return render(request, 'crm/lead_attachment.html', {'form': form, 'lead_detalle': detalle})

"""Se da de baja un lead 
 con toda su estructura"""
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

"""Se inicializa un lead 
etapa de arranque, se crea su checklist"""
@login_required
def lead_init(request, id):
	print 'init de ' + str(id)
	detalle = LeadDetalle.objects.get(id=id)

	if not detalle.es_vigente:
		return redirect('crm:lista_lead')
	if request.method == 'POST':
		form = LeadDetalleForm(request.POST)
		form_comer = InfoComercialForm(request.POST, request.FILES)
		form_finan = InfoFinanzasForm(request.POST, request.FILES)
		print str (form.is_valid()) + str(form_comer.is_valid()) + str(form_finan.is_valid())
		if form.is_valid() and form_comer.is_valid() and form_finan.is_valid():
			lead = Lead.objects.get(id=detalle.lead_id)
			#Se da quita como vigente el lead actual
			detalle.es_vigente = False
			detalle.save()
			#Se guada fecha real de Lead
			fecha = con_factura = request.POST['date']
			if fecha:
				fecha_real_init = datetime.strptime(fecha, '%Y/%M/%d')
				lead.fecha_real_init = fecha_real_init

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

			# se guarda info complementaria
			comercial = form_comer.save()
			finanzas = form_finan.save()
			lead.info_comercial=comercial
			lead.info_finanzas=finanzas
			comercial.folio=lead.folio
			finanzas.folio=lead.folio
			comercial.save()
			finanzas.save()
			lead.save()
			print 'termina arranque'
			return redirect('crm:lista_lead')
		else:
			print 'datos invalidos'
			return render(request, 'crm/lead_form_init.html', {'form': form, 'lead_detalle': detalle,
															   'formComercial':form_comer, 'formFinanzas':form_finan})
	else:
		print 'get'
		form_comer = InfoComercialForm()
		form_finan = InfoFinanzasForm()
		form = LeadDetalleForm(instance=detalle)
		return render(request, 'crm/lead_form_init.html', {'form': form, 'lead_detalle': detalle,
														   'formComercial':form_comer, 'formFinanzas':form_finan})
"""Pasa a la etapa siguiente un lead, 
valida de que etapa viene y se genera 
un nuevo detalle"""
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
				if fecha:
					fecha_plan_init = datetime.strptime(fecha, '%Y/%M/%d')
					lead.fecha_plan_init=fecha_plan_init
			lead.save()
			#Se clona el detalle"
			detalle_new = form.instance
			detalle_new.etapa = new_etapa
			detalle_new.id = None
			detalle_new.lead = lead
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
		form = LeadDetalleForm(instance=detalle)
		for p in detalle.producto.all():
			print p.nombre
		today = timezone.now()
		print today
		print lead.fecha_lnc

		time_life = abs((today - lead.fecha_lnc).days)
		comments = prev_comments(lead)
		contexto = {'form':form, 'lead_detalle':detalle, 'time_life':time_life, 'comments':sorted(comments.items(),reverse=True)}
		return render(request, 'crm/lead_form_next.html', contexto)

"""Muestra el detalle del lead, carga todas 
sus etapas asi como los adjuntos y 
el checklist si es que hay"""
@login_required
def lead_details(request, id):
	print 'deatalles de ' +str (id)
	detalle = LeadDetalle.objects.get(id=id)
	lead = Lead.objects.get(id=detalle.lead_id)
	listLeads = LeadDetalle.objects.filter(lead=lead)
	attachments = Attachment.objects.filter(lead=lead)
	if not detalle.es_vigente:
		return redirect('crm:lista_lead')
	print 'get'
	return render(request, 'crm/lead_details.html', {'object_list': listLeads, 'attachments': attachments, 'lead':lead})

"""Actualiza un lead y redirecciona 
a la pagina de la lista de leads"""
class LeadUpdate(UpdateView):
	model = LeadDetalle
	form_class = LeadDetalleForm
	template_name = 'crm/lead/update.html'
	success_url = reverse_lazy('crm:lista_lead')

'Deprecated'
class LeadDelete(DeleteView):
	model = LeadDetalle
	template_name = 'crm/generic_form_delete.html'
	success_url = reverse_lazy('crm:lista_lead')

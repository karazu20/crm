# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.forms import ModelForm
from crm.models import *

class EjecutivoForm(forms.ModelForm):

	class Meta:
		model = EjecutivoComercial

		fields = [
			'nombre',
			'puesto',
			'mail',
			'telefono',
			'celular',
			#'fecha_ing',
			#'fecha_sal',
			'comentarios',
		]
		labels = {
			'nombre': 'Nombre',
			'puesto': 'Puesto',
			'mail': 'Email',
			'telefono': 'Teléfono',
			'celular': 'Celular',
			#'fecha_ing': 'Fecha de ingreso',
			#'fecha_sal': 'Fecha de salida',
			'comentarios': 'Comentarios',

		}
		widgets = {
			'nombre': forms.TextInput(attrs={'placeholder':"Nombre", 'class':'agulna-clase'}),
			'puesto': forms.TextInput(attrs={'placeholder':"Puesto"}),
			'mail': forms.EmailInput(attrs={'placeholder':"Email"}),
			'telefono': forms.TextInput(attrs={'placeholder':"Teléfono"}),
			'celular': forms.TextInput(attrs={'placeholder':"Celular"}),
			#'fecha_ing': forms.DateInput(attrs={'class':'form-control','placeholder':'YYYY-mm-dd'}),
			#'fecha_sal': forms.DateInput(attrs={'class':'form-control','placeholder':'YYYY-mm-dd'}),
			'comentarios': forms.Textarea(attrs={'placeholder':"Comentarios"}),
		}

class ContactoForm(forms.ModelForm):
	class Meta:
		model = Contacto

		fields = [
			'nombre',
			'puesto_interno',
			'mail',
			'telefono',
			'celular',
			'fecha_nac',
			'direccion',
			'rol',
			'empresa',
			'area',
			'publicidad',
			'comentarios',
		]
		labels = {
			'nombre': 'Nombre',
			'puesto_interno': 'Puesto',
			'mail': 'Email',
			'telefono': 'Teléfono de oficina',
			'celular': 'Célular',
			'fecha_nac': 'Fecha de nacimiento',
			'direccion': 'Dirección de oficina',
			'rol': 'Rol en la empresa',
			'empresa': 'Empresa',
			'area': 'Area',
			'publicidad': 'Publicidad',
			'comentarios': 'Comentarios',

		}
		widgets = {
			'nombre': forms.TextInput(attrs={'placeholder': 'Nombre del contacto'}),
			'puesto_interno': forms.Select(attrs={'placeholder': 'Puesto del contacto'}),
			'mail': forms.EmailInput(attrs={'placeholder': 'Email del contaco'}),
			'telefono': forms.TextInput(attrs={'placeholder': 'Telefono del contacto'}),
			'celular': forms.TextInput(attrs={'placeholder': 'Célular del contacto'}),
			'fecha_nac': forms.DateInput(attrs={ 'placeholder': 'YYYY-mm-dd'}),
			'direccion': forms.TextInput(attrs={'placeholder': 'Dirección del contacto'}),
			'rol': forms.Select(attrs={'placeholder': 'Rol del contacto'}),
			'empresa': forms.Select(attrs={'placeholder': 'Empresa del contacto'}),
			'area': forms.Select(attrs={'placeholder': 'Área del contacto '}),
			'publicidad': forms.CheckboxInput(attrs={'placeholder': 'Publicidad'}),
			'comentarios': forms.Textarea(attrs={'placeholder': 'Comentarios'}),
		}

class EmpresaForm(forms.ModelForm):
	class Meta:
		model = Empresa

		fields = [
			'nombre',
			'razon_social',
			'direccion',
			'industria',
			'tamanio',
			'cobertura',
			'origen',
			'interno',
			'actividad',
			'relacion',
			'comentarios',

		]
		labels = {
			'nombre': 'Nombre',
			'razon_social': 'Razon social',
			'direccion': 'Dirección',
			'industria': 'Industria',
			'tamanio': 'Categoría tamaño',
			'cobertura': 'Categoría cobertura',
			'origen': 'Categoría origen',
			'interno': 'Categoría interna',
			'actividad': 'Estatus actividad',
			'relacion': 'Estatus Relación',
			'comentarios': 'Comentarios',
		}
		widgets = {
			'nombre': forms.TextInput(attrs={'placeholder': 'Nombre de la Empresa'}),
			'razon_social': forms.TextInput(attrs={'placeholder': 'Razón social de la Empresa'}),
			'direccion': forms.TextInput(attrs={'placeholder': 'Dirección de la Empresa'}),
			'industria': forms.Select(attrs={'placeholder': 'Industria de la Empresa'}),
			'tamanio': forms.Select(attrs={'placeholder': 'Tamaño de la Empresa'}),
			'cobertura': forms.Select(attrs={'placeholder': 'Cobertura de la Empresa'}),
			'origen': forms.Select(attrs={'placeholder': 'Origen de la Empresa'}),
			'interno': forms.Select(attrs={'placeholder': 'Categoría de la Empresa'}),
			'actividad': forms.Select(attrs={'placeholder': 'Actividad de la Empresa'}),
			'relacion': forms.Select(attrs={'placeholder': 'Ralación con la Empresa'}),
			'comentarios': forms.Textarea(attrs={'placeholder': 'Agregue sus comentarios'}),

		}

# class LeadForm(forms.ModelForm):
# 	class Meta:
# 		model = Lead
#
# 		fields = [
# 			'empresa',
# 			'contacto',
# 			'ejecutivo',
#
# 		]
# 		labels = {
# 			'empresa': 'Empresa',
# 			'contacto': 'Contacto',
# 			'ejecutivo': 'Ejecutivo',
#
#
# 		}
# 		widgets = {
# 			'empresa': forms.Select(attrs={'class': 'form-control'}),
# 			'contacto': forms.Select(attrs={'class': 'form-control'}),
# 			'ejecutivo': forms.Select(attrs={'class': 'form-control'}),
#


def validate_date(date):
	print 'date valida'
	return True

class LeadDetalleForm(forms.ModelForm):

	# fecha_plan_init = forms.DateField(label="Fecha planeada de inicio",
	# 									initial=None,
	# 									required=False,
	# 									input_formats=['%Y/%m/%d'],
	# 									widget=forms.DateInput(attrs={'class': 'form-control'}, format='%Y/%m/%d'), )
    #
	# fecha_real_init = forms.DateField(label="Fecha real de inicio",
	# 									initial=None,
	# 									required=False,
	# 									input_formats=['%Y/%m/%d'],
	# 									widget=forms.DateInput(attrs={'class': 'form-control'}, format='%Y/%m/%d'), )


	class Meta:
		model = LeadDetalle

		fields = [
			'empresa',
			'contacto',
			'ejecutivo_principal',
			'ejecutivo_primario',
			'ejecutivo_secundario',
			'comentarios',
			'causa_salida',
			'estimado',
			'producto',
			'plaza',
			'fuente',
			#'fecha_plan_init',
			#'fecha_real_init',
		]
		labels = {
			'empresa': 'Empresa',
			'contacto': 'Contacto',
			'ejecutivo_principal':'Ejecutivo responsable',
			'ejecutivo_primario': 'Ejecutivo alterno 1',
			'ejecutivo_secundario': 'Ejecutivo alterno 2',
			'comentarios': 'Comentarios',
			'causa_salida': 'Causa de salida',
			'estimado': 'Estimado',
			'producto': 'Producto',
			'plaza': 'Plaza',
			'fuente': 'Fuente inicial',
			#'fecha_plan_init': 'Fecha planeada de inicio',
			#'fecha_real_init': 'Fecha real de inicio',
		}
		widgets = {
			'empresa': forms.Select(attrs={'placeholder': 'Empresa'}),
			'contacto': forms.Select(attrs={'placeholder': 'Contacto'}),
			'ejecutivo_principal': forms.Select(attrs={'placeholder': 'Ejecutivo responsable'}),
			'ejecutivo_primario': forms.Select(attrs={'placeholder': 'Ejecutivo alterno 1'}),
			'ejecutivo_secundario': forms.Select(attrs={'placeholder': 'Ejecutivo alterno 2'}),
			'comentarios': forms.Textarea(attrs={'placeholder': 'Comentarios'}),
			'causa_salida': forms.TextInput(attrs={'placeholder': 'Causa de salida'}),
			'estimado': forms.TextInput(attrs={'placeholder': 'Monto estimado'}),
			'producto': forms.SelectMultiple(attrs={'placeholder': 'Producto'}),
			'plaza': forms.Select(attrs={'placeholder': 'Plaza'}),
			'fuente': forms.Select(attrs={'placeholder': 'Fuente inicial'}),
			#'fecha_plan_init': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-mm-dd' }),
			#'fecha_real_init': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-mm-dd' }),

		}

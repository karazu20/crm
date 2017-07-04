# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


TIPOS_LEADS = {
	(1,'LNC'),
	(2,'LC'),
	(3,'OP'),
	(4,'NEG'),
	(5,'CIE'),
}


ESTATUS = {
	(1,'Activo'),
	(2,'Inactivo'),
}

PERFIL = {
	(2,'Administrador'),
	(3,'Operativo'),
}


class EtapasLeads(models.Model):
	nombre = models.CharField(max_length=100)
	#descripcion = models.CharField(max_length=300, blank=True)
	estatus = models.IntegerField(default=1, choices=ESTATUS)
	modified = models.DateTimeField(default=timezone.now)

	class Meta:
		ordering = ('id','nombre')
		verbose_name_plural = 'Etapas lead'

	def __str__(self):
		return  self.nombre

		
class CategoriaInterna(models.Model):
	nombre = models.CharField(max_length=100)
	#descripcion = models.CharField(max_length=300, blank=True)
	estatus = models.IntegerField(default=1, choices=ESTATUS)
	modified = models.DateTimeField(default=timezone.now)

	class Meta:
		ordering = ('id','nombre')
		verbose_name_plural = 'Categorias internas'

	def __str__(self):
		return  self.nombre

class EstatusActividad(models.Model):
	nombre = models.CharField(max_length=100)
	#descripcion = models.CharField(max_length=300, blank=True)
	estatus = models.IntegerField(default=1, choices=ESTATUS)
	modified = models.DateTimeField(default=timezone.now)

	class Meta:
		ordering = ('id','nombre')
		verbose_name_plural = 'Estatus de las actividades'

	def __str__(self):
		return self.nombre

class Producto(models.Model):
	nombre = models.CharField(max_length=100)
	#descripcion = models.CharField(max_length=300, blank=True)
	estatus = models.IntegerField(default=1, choices=ESTATUS)
	modified = models.DateTimeField(default=timezone.now)

	class Meta:
		ordering = ('id','nombre')
		verbose_name_plural = 'Productos de ventas'

	def __str__(self):
		return  self.nombre

class CategoriaTamanio(models.Model):
	nombre = models.CharField(max_length=100)
	#descripcion = models.CharField(max_length=300, blank=True)
	estatus = models.IntegerField(default=1, choices=ESTATUS)
	modified = models.DateTimeField(default=timezone.now)

	class Meta:
		ordering = ('id','nombre')
		verbose_name_plural = 'Catagoria de tamaños'

	def __str__(self):
		return  self.nombre


class CategoriaCobertura(models.Model):
	nombre = models.CharField(max_length=100)
	#descripcion = models.CharField(max_length=300, blank=True)
	estatus = models.IntegerField(default=1, choices=ESTATUS)
	modified = models.DateTimeField(default=timezone.now)

	class Meta:
		ordering = ('id','nombre')
		verbose_name_plural = 'Categorias de cobertura'

	def __str__(self):
		return self.nombre


class CategoriaOrigen(models.Model):
	nombre = models.CharField(max_length=100)
	#descripcion = models.CharField(max_length=300, blank=True)
	estatus = models.IntegerField(default=1, choices=ESTATUS)
	modified = models.DateTimeField(default=timezone.now)

	class Meta:
		ordering = ('id','nombre')
		verbose_name_plural = 'Categorias de origen'

	def __str__(self):
		return  self.nombre


class EstatusRelacion(models.Model):
	nombre = models.CharField(max_length=100)
	#descripcion = models.CharField(max_length=300, blank=True)
	estatus = models.IntegerField(default=1, choices=ESTATUS)
	modified = models.DateTimeField(default=timezone.now)

	class Meta:
		ordering = ('id','nombre')
		verbose_name_plural = 'Estatus de la ralación'

	def __str__(self):
		return self.nombre


class PuestoInterno(models.Model):
	nombre = models.CharField(max_length=100)
	#descripcion = models.CharField(max_length=300, blank=True)
	estatus = models.IntegerField(default=1, choices=ESTATUS)
	modified = models.DateTimeField(default=timezone.now)

	class Meta:
		ordering = ('id','nombre')
		verbose_name_plural = 'Puestos internos'

	def __str__(self):
		return  self.nombre


class RolEmpresa(models.Model):
	nombre = models.CharField(max_length=100)
	#descripcion = models.CharField(max_length=300, blank=True)
	estatus = models.IntegerField(default=1, choices=ESTATUS)
	modified = models.DateTimeField(default=timezone.now)

	class Meta:
		ordering = ('id','nombre')
		verbose_name_plural = 'Roles'

	def __str__(self):
		return self.nombre


class FuenteInicial(models.Model):
	nombre = models.CharField(max_length=100)
	#descripcion = models.CharField(max_length=300, blank=True)
	estatus = models.IntegerField(default=1, choices=ESTATUS)
	modified = models.DateTimeField(default=timezone.now)

	class Meta:
		ordering = ('id','nombre')
		verbose_name_plural = 'Fuentes iniciales'

	def __str__(self):
		return  self.nombre


class AreaFuncional(models.Model):
	nombre = models.CharField(max_length=100)
	#descripcion = models.CharField(max_length=300, blank=True)
	estatus = models.IntegerField(default=1, choices=ESTATUS)
	modified = models.DateTimeField(default=timezone.now)

	class Meta:
		ordering = ('id','nombre')
		verbose_name_plural = 'Areas funcionales'

	def __str__(self):
		return self.nombre

class Industria(models.Model):
	nombre = models.CharField(max_length=100)
	#descripcion = models.CharField(max_length=300, blank=True)
	estatus = models.IntegerField(default=1, choices=ESTATUS)
	modified = models.DateTimeField(default=timezone.now)

	class Meta:
		ordering = ('id','nombre')
		verbose_name_plural = 'Industrias'

	def __str__(self):
		return self.nombre


class TipoIndustria(models.Model):
	nombre = models.CharField(max_length=100)
	#descripcion = models.CharField(max_length=300, blank=True)
	estatus = models.IntegerField(default=1, choices=ESTATUS)
	modified = models.DateTimeField(default=timezone.now)

	class Meta:
		ordering = ('id','nombre')
		verbose_name_plural = 'Tipos de industrias'

	def __str__(self):
		return  self.nombre


class Plaza(models.Model):
	nombre = models.CharField(max_length=100)
	#descripcion = models.CharField(max_length=300, blank=True)
	estatus = models.IntegerField(default=1, choices=ESTATUS)
	modified = models.DateTimeField(default=timezone.now)

	class Meta:
		ordering = ('id','nombre')
		verbose_name_plural = 'Plazas'

	def __str__(self):
		return  self.nombre

class Empresa(models.Model):
	nombre = models.CharField(max_length=100)
	razon_social = models.CharField(max_length=300)
	direccion = models.CharField(max_length=500, blank=True)
	comentarios = models.CharField(max_length=2000, blank=True)
	industria = models.ForeignKey(Industria, related_name='empresa_industria', null=True)
	tamanio = models.ForeignKey(CategoriaTamanio, related_name='empresa_tamanio', null=True)
	cobertura = models.ForeignKey(CategoriaCobertura, related_name='empresa_cobertura', null=True)
	origen = models.ForeignKey(CategoriaOrigen, related_name='empresa_origen', null=True)
	interno = models.ForeignKey(CategoriaInterna, related_name='empresa_interno', null=True)
	actividad = models.ForeignKey(EstatusActividad, related_name='empresa_actividad', null=True)
	relacion = models.ForeignKey(EstatusRelacion, related_name='empresa_relacion', null=True)
	date_insert = models.DateTimeField(default=timezone.now)
	date_update = models.DateTimeField(default=timezone.now)
	#user_insert =  models.ForeignKey(User, related_name='empresa_user_insert', null=True)
	#user_update = models.ForeignKey(User, related_name='empresa_user_update', null=True)

	class Meta:
		ordering = ('id','nombre')
		verbose_name_plural = 'Empresas'

	def __str__(self):
		return  self.nombre


class Contacto(models.Model):
	nombre = models.CharField(max_length=100)
	mail = models.EmailField(verbose_name='Correo Electrónico')
	telefono = models.CharField(max_length=20, verbose_name='Teléfono',blank=True)
	celular = models.CharField(max_length=20, verbose_name='Celular',blank=True)
	comentarios = models.CharField(max_length=2000, blank=True)
	fecha_nac = models.DateTimeField(verbose_name='Fecha de Nacimiento', blank=True, null=True)
	direccion = models.CharField(max_length=500, blank=True, verbose_name='Dirreción Oficina')
	puesto_interno = models.ForeignKey(PuestoInterno, related_name='contacto_puesto_interno', null=True)
	rol = models.ForeignKey(RolEmpresa, related_name='contacto_rol', null=True)
	empresa = models.ForeignKey(Empresa, related_name='contacto_empresa', null=True)
	area = models.ForeignKey(AreaFuncional, related_name='contacto_area', null=True)
	publicidad = models.BooleanField(default=True)
	date_insert = models.DateTimeField(default=timezone.now)
	date_update = models.DateTimeField(default=timezone.now)

	#user_insert =  models.ForeignKey(User, related_name='empresa_user_insert', null=True)

	class Meta:
		ordering = ('id','nombre')
		verbose_name_plural = 'Contactos'

	def __str__(self):
		return self.nombre

class EjecutivoComercial(models.Model):
	nombre = models.CharField(max_length=100)
	mail = models.EmailField(verbose_name='Correo Electrónico')
	telefono = models.CharField(max_length=20, verbose_name='Teléfono', blank=True)
	celular = models.CharField(max_length=20, verbose_name='Celular', blank=True)
	comentarios = models.CharField(max_length=2000, blank=True)
	fecha_ing = models.DateTimeField(verbose_name='Fecha de Ingreso',null=True)
	fecha_sal = models.DateTimeField(verbose_name='Fecha de salida', null=True)
	puesto = models.CharField(max_length=100)
	date_insert = models.DateTimeField(default=timezone.now)
	date_update = models.DateTimeField(default=timezone.now)
	user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE, null=True)
	perfil= models.IntegerField(default=2, choices=PERFIL)
	#user_insert =  models.ForeignKey(User, related_name='empresa_user_insert', null=True)
	#user_update = models.ForeignKey(User, related_name='empresa_user_update', null=True)


	#user_insert =  models.ForeignKey(User, related_name='empresa_user_insert', null=True)

	class Meta:
		ordering = ('id','nombre')
		verbose_name_plural = 'Ejecutivos'

	def __str__(self):
		return self.nombre



class Lead(models.Model):
	nombre = models.CharField(max_length=100)
	owner = models.ForeignKey(User, related_name='owner', null=True)
	fecha_lnc = models.DateTimeField(verbose_name='Fecha de lead no calif',  null=True)
	fecha_lc = models.DateTimeField(verbose_name='Fecha de lead calif', null=True)
	fecha_op = models.DateTimeField(verbose_name='Fecha de operación', null=True)
	fecha_neg = models.DateTimeField(verbose_name='Fecha de negociación', null=True)
	fecha_cie = models.DateTimeField(verbose_name='Fecha de cierre', null=True)
	fecha_baja = models.DateTimeField(verbose_name='Fecha de baja', null=True)
	fecha_plan_init = models.DateTimeField(verbose_name='Fecha planeada de inicio', null=True)
	fecha_real_init = models.DateTimeField(verbose_name='Fecha real de inicio', null=True)


	class Meta:
		ordering = ('id', 'nombre')
		verbose_name_plural = 'Leads'

	def __str__(self):
		return self.nombre


class LeadDetalle(models.Model):
	lead = models.ForeignKey(Lead, related_name='lead', null=True)
	empresa = models.ForeignKey(Empresa, related_name='empresa_lead', null=True)
	contacto = models.ForeignKey(Contacto, related_name='contacto_lead', null=True)
	ejecutivo_principal = models.ForeignKey(EjecutivoComercial, related_name='ejecutivo_prin_lead',  null=True)
	ejecutivo_primario = models.ForeignKey(EjecutivoComercial, related_name='ejecutivo_prim_lead', blank=True, null=True)
	ejecutivo_secundario = models.ForeignKey(EjecutivoComercial, related_name='ejecutivo_sec_lead', blank=True, null=True)
	estimado = models.FloatField(null=True)
	comentarios = models.CharField(max_length=2000, blank=True)
	causa_salida = models.CharField(max_length=2000, blank=True, null=True)
	producto = models.ManyToManyField(Producto, related_name='producto_lead')
	plaza = models.ForeignKey(Plaza, related_name='lead_plaza', null=True)
	fuente = models.ForeignKey(FuenteInicial, related_name='lead_fuente', null=True)
	etapa = models.ForeignKey(EtapasLeads, related_name='lead_etapa', default=1, null=False)
	es_vigente= models.BooleanField(default=True)
	#fecha_plan_init = models.DateTimeField(verbose_name='Fecha planeada de inicio', default=timezone.now, blank=True, null=True)
	#fecha_real_init = models.DateTimeField(verbose_name='Fecha real de inicio', default=timezone.now,blank=True, null=True)
	date_insert = models.DateTimeField(default=timezone.now)
	date_update = models.DateTimeField(default=timezone.now)
	#user_insert =  models.ForeignKey(User, related_name='empresa_user_insert', null=True)
	#user_update = models.ForeignKey(User, related_name='empresa_user_update', null=True)


	#user_insert =  models.ForeignKey(User, related_name='empresa_user_insert', null=True)

	class Meta:
		ordering = ('id', 'empresa')
		verbose_name_plural = 'Deatelles Leads'

	def __str__(self):
		return  str (self.empresa)



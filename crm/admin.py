# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from crm.models import *

# Register your models here.

admin.site.register(CategoriaInterna)
admin.site.register(EstatusActividad)
admin.site.register(Producto)
admin.site.register(CategoriaTamanio)
admin.site.register(CategoriaCobertura)
admin.site.register(CategoriaOrigen)
admin.site.register(EstatusRelacion)
admin.site.register(PuestoInterno)
admin.site.register(RolEmpresa)
admin.site.register(FuenteInicial)
admin.site.register(AreaFuncional)
admin.site.register(Industria)
admin.site.register(TipoIndustria)
admin.site.register(Plaza)
admin.site.register(EtapasLeads)

admin.site.register(EjecutivoComercial)
admin.site.register(Empresa)
admin.site.register(Contacto)
admin.site.register(Lead)
admin.site.register(LeadDetalle)
admin.site.register(Attachment)

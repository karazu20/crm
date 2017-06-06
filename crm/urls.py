from django.conf.urls import url
from crm.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^ejecutivo/add/$', login_required(EjecutivoCreate.as_view()), name='crear_ejecutivo'),
    url(r'^ejecutivo/(?P<pk>\d+)/$', login_required(EjecutivoUpdate.as_view()), name='editar_ejecutivo'),
    url(r'^ejecutivo/(?P<pk>\d+)/del/$', login_required(EjecutivoDelete.as_view()), name='eliminar_ejecutivo'),
    url(r'^ejecutivos/$', login_required(EjecutivoList.as_view()), name='lista_ejecutivo'),
   # url(r'^ejecutivos/(?P<pk>\d+)$', EjecutivoList.as_view(), name='lista_ejecutivo'),

    url(r'^empresa/add/$', login_required(EmpresaCreate.as_view()), name='crear_empresa'),
    url(r'^empresa/(?P<pk>\d+)/$', login_required(EmpresaUpdate.as_view()), name='editar_empresa'),
    url(r'^empresa/(?P<pk>\d+)/del/$', login_required(EmpresaDelete.as_view()), name='eliminar_empresa'),
    url(r'^empresas/$', login_required(EmpresaList.as_view()), name='lista_empresa'),
    #
    url(r'^contacto/add/$', login_required(ContactoCreate.as_view()), name='crear_contacto'),
    url(r'^contacto/(?P<pk>\d+)/$', login_required(ContactoUpdate.as_view()), name='editar_contacto'),
    url(r'^contacto/(?P<pk>\d+)/del/$', login_required(ContactoDelete.as_view()), name='eliminar_contacto'),
    url(r'^contactos/$', login_required(ContactoList.as_view()), name='lista_contacto'),

    url(r'^lead/add/$', lead_create, name='crear_lead'),
    url(r'^lead/(?P<pk>\d+)/$', LeadUpdate.as_view(), name='editar_lead'),
    url(r'^lead/(?P<id>\d+)/next/$', lead_next, name='avanzar_lead'),
    url(r'^lead/(?P<id>\d+)/del/$', lead_baja, name='baja_lead'),
    url(r'^leads/$', LeadList.as_view(), name='lista_lead'),
    url(r'^lead/(?P<id>\d+)/init/$', lead_init, name='arrancar_lead'),

]

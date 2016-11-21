from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^$',index_view,name='index_view'),
	url(r'^login/$','django.contrib.auth.views.login',{'template_name':'voto/login.html'}, name='login'),
	url(r'^registro_de_usuarios/$',signup.as_view(),name='registro_de_usuarios'),
	url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
	url(r'^panel_admin$',admin,name='admin_panel'),
	url(r'^panel_admin/encuestaadmin/$', EncuestaAdmin, name="encuesta_admin"),
	url(r'^panel_admin/encuestaadmin/Crear_Categoria/$', Crear_Categoria.as_view(), name='crear_categoria_view'),
	url(r'^panel_admin/encuestaadmin/Crear_Encuesta/$',Crear_Encuesta.as_view(), name='crear_encuesta' ),
	url(r'^panel_admin/encuestaadmin/encuesta_lista/$',encuesta_lista,name='encuesta_lista'),
	url(r'^panel_admin/encuestaadmin/encuesta_lista/encuesta_detalle/(?P<id>\d+)/$', encuesta_detalle, name='encuesta_detalle'),
	url(r'^panel_admin/encuestaadmin/encuesta_lista/borrar_encuesta/(?P<id>\d+)/$', borrar_encuesta, name='borrar_encuesta'),
	url(r'^panel_admin/encuestaadmin/encuesta_lista/actualizar_encuesta/(?P<id>\d+)/$', actualizar_encuesta, name='actualizar_encuesta'),
	url(r'^encuesta/$', EncuestaView.as_view(), name='encuestaview'),
	url(r'^buscar$', buscar2, name= 'buscar'),
]

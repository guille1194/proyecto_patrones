from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.views.generic import FormView, CreateView, ListView,DetailView,UpdateView,DeleteView
from .forms import Userform, EncuestaForm
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from .models import Usuario, Encuesta, Categoria, Eleccion, Voto
from django.core.paginator import Paginator, EmptyPage, InvalidPage, PageNotAnInteger
from django.contrib.auth.models import User
# Create your views here.

def index_view(request):
	queryset_list = Encuesta.objects.all().order_by('-fecha_creacion')
	paginator = Paginator(queryset_list, 3)

	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)
		context = {
			"object_list": queryset
		}
	return render(request,'voto/index.html', context)

class signup(FormView):
	template_name='voto/signup.html'
	form_class = Userform
	success_url = reverse_lazy('index_view')

	def form_valid(self,form):
		user = form.save()
		p = Usuario()
		p.user_perfil = user
		p.mail = form.cleaned_data['mail']
		p.name = form.cleaned_data['name']
		p.last = form.cleaned_data['last']
		p.save()
		return super(signup,self).form_valid(form)


def admin(request):
	return render(request, 'voto/Admin.html')

class Crear_Categoria(ListView):
	template_name = 'voto/CrearCategoria.html'
	model = Categoria
	fields = '__all__'
	success_url = reverse_lazy('admin_panel')

def encuesta_detalle(request, id=None):
	encuesta = get_object_or_404(Encuesta, ID_Encuesta=id)
	context = {
		"object_list": "eee",
		"encuesta": encuesta,
	}
	return render(request, "voto/encuesta_detalle", context)

def encuesta_lista(request):
	queryset_list = Encuesta.objects.all().order_by('-fecha_creacion')
	paginator = Paginator(queryset_list, 3) # Show 3 contacts per page

	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)
	context = {
		"object_list": queryset
	}
	return render(request, "voto/encuesta_lista.html", context)

def EncuestaAdmin(request):
	return render(request, "voto/encuestaadmin.html")

class Crear_Encuesta(FormView):
	template_name = 'voto/CrearEncuesta.html'
	form_class = EncuestaForm
	success_url = reverse_lazy('encuesta_lista')

	def form_valid(self,form):
		p = Encuesta()
		p.titulo = form.cleaned_data['titulo']
		p.categoria = form.cleaned_data['categoria']
		p.fecha_creacion = date.today()
		p.publicado = form.cleaned_data['publicado']
		p.propietario = form.cleaned_data['propietario']
		p.save()
		return super(Crear_Encuesta, self).form_valid(form)

	def get_context_data(self, **kwargs):
		ctx = super(Crear_Encuesta, self).get_context_data(**kwargs)
		ctx['Categoria'] = Categoria.objects.all()
		ctx['Usuario'] = Usuario.objects.all()
		return ctx

class Encuesta(ListView):
	template_name = 'voto/Encuesta.html'
	model = Encuesta
	fields = '__all__'

def buscar2(request):
	if request.POST:
		data = request.POST['campo']
		p = Encuesta.objects.filter(titulo=data)
		ctx = {'objects': p}
	else:
		ctx = {'mensaje':'no hay datos..'}
	return render(request, 'voto/buscar2.html', ctx)

def borrar_encuesta(request, id=None):
	encuesta = get_object_or_404(Encuesta, ID_Encuesta=id)
	encuesta.delete()
	return redirect('encuesta_lista')

def actualizar_encuesta(request, id):
	encuesta = get_object_or_404(Encuesta, ID_Encuesta=id)
	form = EncuestaForm(request.POST or None, request.FILES or None, instance=encuesta)
	if form.is_valid():
		try:
			encuesta = form.save()
			encuesta.save()
			context = {
				"encuesta":encuesta,
			}
			return render(request, "voto/encuesta_detalle.html", context)
		except:
			print "Un error"
	context = {
		"object_list": "eee",
		"encuesta": encuesta,
		"form":form,
		"Categoria": Categoria.objects.all()
	}
	return render(request, "voto/actualizar_encuesta.html", context)

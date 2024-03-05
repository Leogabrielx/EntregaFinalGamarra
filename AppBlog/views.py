from django.shortcuts import render, redirect
from AppBlog.models import Categoria, Articulo, Comentario
from AppBlog.forms import CategoriaFormulario, ArticuloFormulario, ComentarioForm
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.contrib.auth.decorators import login_required


# Create your views here.
def homepage(request):
    articulos = Articulo.objects.order_by('-fecha_publicacion')
    
    if request.GET.get("busqueda"):
        busqueda = request.GET.get("busqueda")
        if busqueda:
            articulos = Articulo.objects.filter(Q(titulo__icontains=busqueda) | Q(autor__username__icontains=busqueda) | Q(categoria__nombre__icontains=busqueda))
    
    return render(request, 'inicio.html', {'articulos': articulos})

def about_us(request):
    return render(request, 'acerca_de_nosotros.html')

@login_required(login_url='/cuentas/login')
def mis_articulos(request):
    articulos = Articulo.objects.filter(autor=request.user).order_by('-fecha_publicacion')
    
    return render(request, 'mis_articulos.html', {'articulos': articulos})

# CATEGORIAS

class CategoriaCreateView(LoginRequiredMixin, CreateView):
    model = Categoria
    template_name = 'crear_categoria.html'
    fields = ['nombre']
    success_url = reverse_lazy('categorias')
    
class CategoriaDeleteView(LoginRequiredMixin, DeleteView):
    model = Categoria
    template_name = "eliminar_categoria.html"
    success_url = reverse_lazy('categorias')
    
    #Validamos que solo puedan eliminar categorias los administradores
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.infoextra.es_admin == False:
            raise Http404("No tienes permiso para eliminar esta categoria.")
        return super().dispatch(request, *args, **kwargs)
    
class CategoriaDetailView(DetailView):
    model = Categoria
    template_name = "detalle_categoria.html"
    success_url = reverse_lazy('categorias')
    
class CategoriaListView(ListView):
    model = Categoria
    context_object_name = 'listado_categorias'
    template_name = "listar_categorias.html"
    
    def get_queryset(self):
        nombre = self.request.GET.get('nombre', '')
        if nombre:
            categorias = self.model.objects.filter(nombre__icontains=nombre)
        else:
            categorias = self.model.objects.all()
        return categorias

class CategoriaUpdateView(LoginRequiredMixin, UpdateView):
    model = Categoria
    template_name = "editar_categoria.html"
    fields = ['nombre']
    success_url = reverse_lazy('categorias')
    
    #Validamos que solo puedan editar categorias los administradores
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.infoextra.es_admin == False:
            raise Http404("No tienes permiso para editar esta categoria.")
        return super().dispatch(request, *args, **kwargs)

# ARTICULOS

class ArticuloCreateView(LoginRequiredMixin, CreateView):
    model = Articulo
    template_name = 'crear_articulo.html'
    form_class = ArticuloFormulario
    success_url = reverse_lazy('mis_articulos')
    
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
    
class ArticuloDeleteView(LoginRequiredMixin, DeleteView):
    model = Articulo
    template_name = "eliminar_articulo.html"
    success_url = reverse_lazy('mis_articulos')
    
    #Validamos que solo puedan eliminar articulos sus autores o los administradores
    def dispatch(self, request, *args, **kwargs):
        articulo = self.get_object()
        if articulo.autor != self.request.user and self.request.user.infoextra.es_admin == False:
            raise Http404("No tienes permiso para eliminar este artículo.")
        return super().dispatch(request, *args, **kwargs)
    
class ArticuloDetailView(DetailView):
    model = Articulo
    template_name = "detalle_articulo.html"
    success_url = reverse_lazy('articulos')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comentarios = Comentario.objects.filter(articulo=self.object)
        context['comentarios'] = comentarios
        return context
    
class ArticuloListView(ListView):
    model = Articulo
    context_object_name = 'listado_articulos'
    template_name = "listar_articulos.html"
    
    def get_queryset(self):
        titulo = self.request.GET.get('titulo', '')
        if titulo:
            articulos = self.model.objects.filter(titulo__icontains=titulo)
        else:
            articulos = self.model.objects.all()
        return articulos

class ArticuloUpdateView(LoginRequiredMixin, UpdateView):
    model = Articulo
    template_name = "editar_articulo.html"
    form_class = ArticuloFormulario
    success_url = reverse_lazy('mis_articulos')
    
    #Validamos que solo puedan editar articulos sus autores o los administradores
    def dispatch(self, request, *args, **kwargs):
        articulo = self.get_object()
        if articulo.autor != self.request.user and self.request.user.infoextra.es_admin == False:
            raise Http404("No tienes permiso para editar este artículo.")
        return super().dispatch(request, *args, **kwargs)
    
# COMENTARIOS

class ComentarioCreateView(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = ComentarioForm
    template_name = 'comentario_form.html'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        form.instance.articulo = Articulo.objects.get(pk=self.kwargs['articulo_id'])
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('detalle_articulo', args=[str(self.kwargs['articulo_id'])])

class ComentarioUpdateView(LoginRequiredMixin, UpdateView):
    model = Comentario
    form_class = ComentarioForm 
    template_name = 'comentario_form.html'

    def get_success_url(self):
        return reverse('detalle_articulo', args=[str(self.object.articulo.pk)])
    
class ComentarioDeleteView(DeleteView):
    model = Comentario
    template_name = 'comentario_confirm_delete.html'

    def get_success_url(self):
        return reverse('detalle_articulo', args=[str(self.object.articulo.pk)])
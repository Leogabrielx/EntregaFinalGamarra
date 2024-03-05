from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login as django_login
from cuentas.models import InfoExtra
from cuentas.forms import NuestroFormularioDeRegistro, NuestroFormularioDeEditarPerfil, CambiarPasswordForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('homepage')  # Redirige a la página principal después de cerrar sesión


# Create your views here.
def login(request):
    error_message = None
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            username = formulario.cleaned_data.get('username')
            password = formulario.cleaned_data.get('password')
            
            usuario = authenticate(username=username, password=password)
            
            django_login(request, usuario)
            
            InfoExtra.objects.get_or_create(user=usuario)
            
            return redirect('homepage')
        
        else:
            error_message = "Credenciales incorrectas. Por favor, inténtalo de nuevo."
    else:
        formulario = AuthenticationForm()
        
    return render(request, 'login.html', {'formulario': formulario, 'error_message': error_message})

def register(request):
    error_message = None
    if request.method == 'POST':
        formulario = NuestroFormularioDeRegistro(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('login')
        else:
            error_message = "Datos incorrectos. Por favor, inténtalo de nuevo."
    else:
        formulario = NuestroFormularioDeRegistro()
        
    return render(request, 'register.html', {'formulario': formulario, 'error_message': error_message})

@login_required
def ver_perfil(request):
    info_extra = request.user.infoextra
    
    return render(request, 'ver_perfil.html', {'info_extra': info_extra})

@login_required
def editar_perfil(request):
    
    info_extra = request.user.infoextra
    
    if request.method == 'POST':
        formulario = NuestroFormularioDeEditarPerfil(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            
            info_extra.link = formulario.cleaned_data.get('link')
            if formulario.cleaned_data.get('avatar'):
                info_extra.avatar = formulario.cleaned_data.get('avatar')
            info_extra.save()
            
            formulario.save()
            return redirect('homepage')
    else:
        formulario = NuestroFormularioDeEditarPerfil(initial={'link': info_extra.link, 'avatar': info_extra.avatar}, instance=request.user)
    return render(request, 'editar_perfil.html', {'formulario': formulario})

class CambiarPassword(LoginRequiredMixin, PasswordChangeView):
    template_name = 'editar_pass.html'
    form_class = CambiarPasswordForm
    success_url = reverse_lazy('editar_perfil')

    def form_invalid(self, form):
        return render(self.request, self.template_name, {'form': form})



from django.urls import path
from cuentas.views import login, register, editar_perfil, CambiarPassword, ver_perfil, logout_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),  
    path('logout/', logout_view, name='logout'),  # Esta línea define la URL 'logout' que usas en tu template
    path('perfil/ver/', ver_perfil, name='ver_perfil'),
    path('perfil/editar/', editar_perfil, name='editar_perfil'),
    path('perfil/editar/password/', CambiarPassword.as_view(), name='editar_pass'),
]

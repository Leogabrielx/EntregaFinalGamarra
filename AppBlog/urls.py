from django.urls import path, include
from . import views
from AppBlog.views import mis_articulos, about_us

urlpatterns = [
    
    path('categorias', views.CategoriaListView.as_view(), name="categorias"),
    path('categorias/crear', views.CategoriaCreateView.as_view(), name="crear_categoria"),
    path('categorias/<int:pk>/', views.CategoriaDetailView.as_view(), name="detalle_categoria"),
    path('categorias/<int:pk>/editar', views.CategoriaUpdateView.as_view(), name="editar_categoria"),
    path('categorias/<int:pk>/eliminar', views.CategoriaDeleteView.as_view(), name="eliminar_categoria"),
    
    path('articulos', views.ArticuloListView.as_view(), name="articulos"),
    path('articulos/crear', views.ArticuloCreateView.as_view(), name="crear_articulo"),
    path('articulos/<int:pk>/', views.ArticuloDetailView.as_view(), name="detalle_articulo"),
    path('articulos/<int:pk>/editar', views.ArticuloUpdateView.as_view(), name="editar_articulo"),
    path('articulos/<int:pk>/eliminar', views.ArticuloDeleteView.as_view(), name="eliminar_articulo"),
    
    path('mis_articulos', mis_articulos, name="mis_articulos"),
    
    path('about_us', about_us, name='about_us'),
    
    path('articulo/<int:articulo_id>/comentario/nuevo/', views.ComentarioCreateView.as_view(), name='nuevo_comentario'),
    path('comentario/<int:pk>/editar/', views.ComentarioUpdateView.as_view(), name='editar_comentario'),
    path('comentario/<int:pk>/eliminar/', views.ComentarioDeleteView.as_view(), name='eliminar_comentario'),
]
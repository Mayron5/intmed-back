from django.contrib import admin
from django.urls import path
from django.urls import re_path

from medicar.views import AgendasViewSet, ConsultasViewSet, EspecialidadesViewSet, Login, UsuariosViewSet

#Rotas da API

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('usuario/login', Login.as_view()),
    re_path('usuarios', UsuariosViewSet.as_view()),
    re_path('agendas', AgendasViewSet.as_view()),
    re_path('consultas', ConsultasViewSet.as_view()),
    re_path('especialidades', EspecialidadesViewSet.as_view())
]

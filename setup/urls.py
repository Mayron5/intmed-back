from django.contrib import admin
from django.urls import path, include
from django.urls import re_path

from rest_framework import routers

from medicar.views import AgendasViewSet, ConsultasViewSet, EspecialidadesViewSet, Login, MedicosViewSet, UsuariosViewSet

router = routers.DefaultRouter()
router.register('medicos', MedicosViewSet)

#Rotas da API
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    re_path('usuarios', UsuariosViewSet.as_view()),
    re_path('usuario/login', Login.as_view()),
    re_path('agendas', AgendasViewSet.as_view()),
    re_path('consultas', ConsultasViewSet.as_view()),
    re_path('especialidades', EspecialidadesViewSet.as_view())
]

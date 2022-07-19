from django.contrib import admin
from django.urls import path, include
from django.urls import re_path

from rest_framework import routers

from medicar.views import AgendasViewSet, ConsultasViewSet, EspecialidadesView, Login, MedicosViewSet, UsuariosViewSet

router = routers.DefaultRouter()
router.register('medicos', MedicosViewSet)
router.register('agendas', AgendasViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    re_path('usuarios', UsuariosViewSet.as_view()),
    re_path('usuario/login', Login.as_view()),
    re_path('consultas', ConsultasViewSet.as_view()),
    re_path('especialidades', EspecialidadesView.as_view())
]

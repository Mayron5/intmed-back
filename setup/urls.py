from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from medicar.views import AgendasViewSet, Login, MedicosViewSet, UsuariosViewSet

router = routers.DefaultRouter()
router.register('usuarios', UsuariosViewSet)
router.register('medicos', MedicosViewSet)
router.register('agendas', AgendasViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('usuario/<str:email>/<str:senha>/login/', Login.as_view())
]

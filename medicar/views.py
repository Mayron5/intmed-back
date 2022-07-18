from rest_framework import viewsets, generics
from medicar.models import Agenda, Medico, Usuario
from medicar.serializers import AgendaSerializer, MedicoSerializer, UsuarioSerializer

class UsuariosViewSet(viewsets.ModelViewSet):
    """Listando todos os usuários"""
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class MedicosViewSet(viewsets.ModelViewSet):
    """Listando todos os médicos"""
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

class AgendasViewSet(viewsets.ModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer

class Login(generics.ListAPIView):

    def get_queryset(self):
        queryset = Usuario.objects.filter(email = self.kwargs['email'], senha = self.kwargs['senha'])
        return queryset

    serializer_class = UsuarioSerializer
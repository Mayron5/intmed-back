from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework.filters import SearchFilter
from medicar.models import Agenda, Consulta, Horario, Medico, Usuario
from medicar.serializers import AgendaSerializer, ConsultaSerializer, MedicoSerializer, UsuarioSerializer


class UsuariosViewSet(viewsets.ModelViewSet):
    """Listando todos os usuários"""
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class MedicosViewSet(viewsets.ModelViewSet):
    """Listando todos os médicos"""
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    filter_backends = [SearchFilter]
    search_fields = ['especialidade__nome']


class AgendasViewSet(viewsets.ModelViewSet):

    queryset = Agenda.objects.filter(dia__range=['2022-07-19', '2022-07-19'])
    filter_backends = [SearchFilter]
    search_fields = ['medico__id']
    serializer_class = AgendaSerializer


class Login(APIView):

    serializer_class = UsuarioSerializer
    
    def get_queryset(self):
        queryset = Usuario.objects.all()
        return queryset

    def post(self, request, *args, **kwargs):
        usuarios = self.get_queryset()
        dados_login = request.data
        
        usuario = usuarios.filter(email=dados_login['email'], senha=dados_login['senha'])
        serializer = UsuarioSerializer(usuario, many=True)
        
        if len(serializer.data) > 0:
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(status=status.HTTP_404_NOT_FOUND)
        

class ConsultasViewSet(APIView):
    serializer_class = ConsultaSerializer

    def get_queryset(self):
        consultas = Consulta.objects.all()
        return consultas

    def get(self, request, *args, **kwargs):
        consultas = self.get_queryset()
        serializer = ConsultaSerializer(consultas, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        dados_consulta = request.data

        dados_horario = Horario.objects.get(
            horario=dados_consulta['horario']
        )
        
        if not dados_horario.disponivel:
            raise APIException('Horário não disponível')

        dados_agenda = Agenda.objects.get(
            pk=dados_consulta['agenda_id'])
        
        dados_usuario = Usuario.objects.get(
            pk=1
        )
        nova_consulta = Consulta.objects.create(
            dia=dados_agenda.dia, horario=dados_consulta['horario'], agenda=dados_agenda, usuario=dados_usuario)
        
        nova_consulta.save()
        
        dados_horario.disponivel = False
        dados_horario.save()
        
        serializer = ConsultaSerializer(nova_consulta)
        return Response(serializer.data)


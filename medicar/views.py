from datetime import date, datetime
import re
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework.filters import SearchFilter
from medicar.models import Agenda, Consulta, Especialidade, Horario, Medico, Usuario
from medicar.serializers import AgendaSerializer, ConsultaSerializer, EspecialidadeSerializer, MedicoSerializer, UsuarioSerializer
from medicar.validators import valida_dia


class UsuariosViewSet(APIView):

    serializer_class = UsuarioSerializer

    def get_queryset(self):
        queryset = Usuario.objects.all()
        return queryset

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = UsuarioSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        dados_usuario = request.data

        usuario = self.get_queryset().filter(email=dados_usuario['email'])

        if usuario:
            return Response(status=status.HTTP_302_FOUND, data='O email informado já existe')

        novo_usuario = Usuario.objects.create(
            nome=dados_usuario['nome'], email=dados_usuario['email'], senha=dados_usuario['senha'])
        novo_usuario.save()

        serializer = UsuarioSerializer(novo_usuario)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class EspecialidadesView(APIView):
    serializer_class = EspecialidadeSerializer

    def get_queryset(self):
        queryset = Especialidade.objects.all()
        return queryset

    def get(self, request, *args, **kwargs):
        especialidades = self.get_queryset()
        serializer = EspecialidadeSerializer(especialidades, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MedicosViewSet(viewsets.ModelViewSet):
    """Listando todos os médicos"""
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    filter_backends = [SearchFilter]
    search_fields = ['especialidade__id']


class AgendasViewSet(APIView):

    serializer_class = AgendaSerializer
    
    def get_queryset(self):
        agendas = Agenda.objects.all()
        return agendas
    
    def get(self, request, *args, **kwargs):
        agendas = self.get_queryset()
        
        if request.GET.get('medico'):
            agendas = agendas.filter(medico__id = request.GET.get('medico'))
            
        if request.GET.get('especialidade'):
            agendas = agendas.filter(medico__especialidade__id = request.GET.get('especialidade'))
            
        serializer = AgendaSerializer(agendas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        


class Login(APIView):

    serializer_class = UsuarioSerializer

    def get_queryset(self):
        queryset = Usuario.objects.all()
        return queryset

    def post(self, request, *args, **kwargs):
        usuarios = self.get_queryset()
        dados_login = request.data

        usuario = usuarios.filter(
            email=dados_login['email'], senha=dados_login['senha'])
        serializer = UsuarioSerializer(usuario, many=True)

        if len(serializer.data) > 0:
            return Response(serializer.data[0], status=status.HTTP_200_OK)

        return Response(status=status.HTTP_404_NOT_FOUND)


class ConsultasViewSet(APIView):
    serializer_class = ConsultaSerializer

    def get_queryset(self):
        consultas = Consulta.objects.all()
        return consultas

    def get(self, request, *args, **kwargs):
        consultas = self.get_queryset().filter(usuario__id=request.GET.get('userid'))
        serializer = ConsultaSerializer(consultas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        dados_consulta = request.data

        dados_horario = Horario.objects.get(
            horario=dados_consulta['horario']
        )

        if not dados_horario.disponivel:
            raise APIException('Horário não disponível')

        dados_agenda = Agenda.objects.get(
            pk=dados_consulta['agenda_id'])

        dados_usuario = Usuario.objects.get(pk=1)
        nova_consulta = Consulta.objects.create(
            dia=dados_agenda.dia, horario=dados_consulta['horario'], agenda=dados_agenda, usuario=dados_usuario)

        nova_consulta.save()

        dados_horario.disponivel = False
        dados_horario.save()

        serializer = ConsultaSerializer(nova_consulta)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        
        try:
            consulta = self.get_queryset().get(id=request.GET.get('id'))
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if not valida_dia(consulta.dia):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        horario = Horario.objects.get(horario = consulta.horario)
        horario.disponivel = True
        horario.save()

        consulta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

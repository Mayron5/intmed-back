from rest_framework import serializers

from medicar.models import Agenda, Consulta, Horario, Medico, Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        exclude = ('senha', )


class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = '__all__'
        
        depth = 1


class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model: Horario
        fields = ('horarios', )
        depth = 2

class AgendaSerializer(serializers.ModelSerializer):
    horarios = serializers.StringRelatedField(many=True)
    class Meta: 
        model = Agenda
        fields = '__all__'

        depth = 3


class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__'
        depth = 3
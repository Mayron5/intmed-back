from rest_framework import serializers

from medicar.models import Agenda, Medico, Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = '__all__'


class AgendaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Agenda
        fields = '__all__'
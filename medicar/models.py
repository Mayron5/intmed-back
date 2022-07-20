from django.db import models
from django.forms import ValidationError

from medicar.validators import valida_dia


class Usuario(models.Model):
    nome = models.CharField(max_length=45)
    email = models.EmailField(blank=False, null=False,
                              unique=True, max_length=30)
    senha = models.CharField(max_length=12)

    def __str__(self) -> str:
        return self.nome


class Especialidade(models.Model):
    nome = models.CharField(max_length=45)

    def __str__(self) -> str:
        return self.nome


class Medico(models.Model):
    crm = models.IntegerField(unique=True)
    nome = models.CharField(max_length=45)
    email = models.CharField(null=True, blank=True, max_length=30)
    especialidade = models.ForeignKey(Especialidade, models.CASCADE)

    def __str__(self) -> str:
        return self.nome


class Agenda(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    dia = models.DateField(max_length=10)

    class Meta:
        unique_together = ('medico', 'dia', )

    def clean(self):
        if not valida_dia(self.dia):
            raise ValidationError(
                'Não é possível agendar para uma data passada!')
        return self.dia

    def __str__(self):
        return 'Agenda do (a)' + self.medico.nome + ' do dia - ' + str(self.dia)


class Horario(models.Model):
    agenda = models.ForeignKey(
        Agenda, on_delete=models.CASCADE, related_name='horarios')
    horario = models.TimeField()
    disponivel = models.BooleanField(default=False)

    class Meta:
        unique_together = ('horario', 'agenda', )

    def __str__(self):
        return str(self.horario)


class Consulta(models.Model):
    dia = models.DateField()
    horario = models.TimeField()
    data_agendamento = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, models.CASCADE)
    agenda = models.ForeignKey(Agenda, models.CASCADE)

    def __str__(self):
        return str(' Paciente - ' + self.usuario.nome)

from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=45)
    email = models.EmailField(blank=False, null=False, unique=True, max_length=30)
    senha = models.CharField(max_length=12)

    def __str__(self) -> str:
        return self.nome

class Medico(models.Model):
    crm = models.IntegerField()
    nome = models.CharField(max_length=45)
    email = models.CharField(null=True, blank=True, max_length=30)

    def __str__(self) -> str:
        return self.nome


class Agenda(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    dia = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.dia


class Horario(models.Model):
    horario = models.CharField(max_length=6, unique=True)
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.horario
from django.contrib import admin
from medicar.models import Agenda, Consulta, Especialidade, Horario, Medico


class Medicos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'especialidade', 'crm')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', 'crm', )
    list_per_page = 10


admin.site.register(Medico, Medicos)


class Agendas(admin.ModelAdmin):
    list_display = ('id', 'medico', 'dia')
    search_fields = ('medico', 'dia', )
    list_per_page = 10


admin.site.register(Agenda, Agendas)


class Horarios(admin.ModelAdmin):
    list_display = ('id', 'agenda', 'horario', 'disponivel')
    list_display_links = ('agenda', )
    search_fields = ('horario', )
    list_per_page = 10


admin.site.register(Horario, Horarios)


class Consultas(admin.ModelAdmin):
    list_display = ('id', 'dia', 'horario', 'usuario', 'agenda')
    list_display_links = ('agenda', 'id', )
    search_fields = ('dia', )
    list_per_page= 10

admin.site.register(Consulta, Consultas)
admin.site.register(Especialidade)
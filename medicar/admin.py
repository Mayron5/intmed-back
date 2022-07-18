from django.contrib import admin

from medicar.models import Agenda, Horario, Medico


class Medicos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'crm')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', 'crm', )
    list_per_page = 10


admin.site.register(Medico, Medicos)


class Agendas(admin.ModelAdmin):
    list_display = ('id', 'medico', 'dia')
    list_display_links = ('id', 'medico')
    search_fields = ('medico', 'dia', )
    list_per_page = 10


admin.site.register(Agenda, Agendas)


class Horarios(admin.ModelAdmin):
    list_display = ('id', 'agenda')
    list_display_links = ('id', )
    list_per_page = 10


admin.site.register(Horario, Horarios)

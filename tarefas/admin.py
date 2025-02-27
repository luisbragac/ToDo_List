from django.contrib import admin
from tarefas.models import Tarefa

class Adicionar_Tarefas(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'concluida')
    list_display_links = ('id', 'titulo')
    list_editable = ('concluida',)
    list_per_page = 10
    search_fields = ('titulo',)

admin.site.register(Tarefa, Adicionar_Tarefas)
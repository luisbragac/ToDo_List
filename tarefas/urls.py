from django.urls import path
from tarefas.views import index, task_detalhes, excluir_task, marcar_concluida, criar_task

urlpatterns = [
    path('', index, name='index'),
    path('detalhe/task_<int:id>/', task_detalhes, name='detalhe'),
    path('tarefa/<int:id>/excluir/', excluir_task, name='excluir_task'),
    path('tarefa//<int:id>/concluida/', marcar_concluida, name='marcar_concluida'),
    path('criar_task/', criar_task, name='criar_task')
]

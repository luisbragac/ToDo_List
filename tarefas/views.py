from django.shortcuts import render, redirect, get_object_or_404
from tarefas.forms import TarefaForms
from tarefas.models import Tarefa
from django.contrib import messages

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Faça login para continuar')
        return redirect('login')


    tarefas = Tarefa.objects.filter(usuario = request.user)
    return render(request, 'tarefas/index.html', {'tarefas': tarefas})

def task_detalhes(request, id):
    tarefas = get_object_or_404(Tarefa, id=id)
    
    return render(request, 'tarefas/task_detalhes.html', {'tarefas':tarefas})

def excluir_task(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    tarefa.delete()

    return redirect('index')

def marcar_concluida(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    tarefa.concluida = True
    tarefa.save()

    return redirect('detalhe', id = tarefa.id)
    
def criar_task(request):
    form = TarefaForms()
    if request.method == 'POST':
        form = TarefaForms(request.POST)

        if form.is_valid():
            titulo = form.cleaned_data['titulo_tarefa']
            descricao = form.cleaned_data['descricao_tarefa']
            data = form.cleaned_data['data']
            prioridade = form.cleaned_data['prioridade']

            tarefa = Tarefa.objects.create(
                usuario = request.user,
                titulo = titulo,
                descricao = descricao,
                data= data,
                prioridade = prioridade,
            )
            tarefa.save()
            
            return redirect('index')

    return render(request, 'tarefas/criar_task.html', {'form':form})
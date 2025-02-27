from django import forms

class TarefaForms(forms.Form):
    titulo_tarefa = forms.CharField(
        label='Título',
        required=True,
        max_length=100,
    )

    descricao_tarefa = forms.CharField(
        label='Descrição',
        max_length=150,
        widget=forms.Textarea(
            attrs={'rows':4}
        )
    )

    data = forms.DateField(
        label='Data',
        required=True,
        widget=forms.DateInput(
            attrs={'type':'date'}
        )
    )

    prioridade = forms.ChoiceField(
        label='Prioridade',
        choices=(
            ('Alta','Alta'),
            ('Média','Média'),
            ('Baixa','Baixa'),
        )
    )
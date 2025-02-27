from django import forms

class CadastroForm(forms.Form):
    nome_cadastro = forms.CharField(
        label='Nome',
        max_length=50,
        required=True,
    )

    email = forms.EmailField(
        label='Email',
        required=True,
        widget=forms.EmailInput
    )


    senha_1 = forms.CharField(
        label='Senha',
        max_length=50,
        required=True,
        widget=forms.PasswordInput(

        )
    )

    senha_2 = forms.CharField(
        label='Confirmar Senha',
        max_length=50,
        required=True,
        widget=forms.PasswordInput(

        )
    )

class LoginForm(forms.Form):
    nome_login = forms.CharField(
        label='Nome',
        max_length=50,
        required=True,
    )

    senha = forms.CharField(
        label='Senha',
        max_length=50,
        required=True,
        widget=forms.PasswordInput(

        )
    )
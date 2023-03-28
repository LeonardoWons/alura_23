from django import forms


class LoginForms(forms.Form):
    nome_login = forms.CharField(label="nome de login", required=True, max_length=100,
                                 widget=forms.TextInput(attrs={"class": "form-control",
                                                               "placeholder": "Digite seu nome"}))
    senha = forms.CharField(label="senha", required=True, max_length=70,
                            widget=forms.PasswordInput(attrs={"class": "form-control",
                                                              "placeholder": "Digite sua senha"}))


class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(label="Nome de cadastro", required=True, max_length=100,
                                    widget=forms.TextInput(attrs={"class": "form-control",
                                                                  "placeholder": "Digite seu nome"}))

    email = forms.EmailField(label="Email", required=True, max_length=100,
                             widget=forms.EmailInput(attrs={"class": "form-control",
                                                            "placeholder": "Digite seu email"}))

    password1 = forms.CharField(label="Senha", required=True, max_length=70,
                                widget=forms.PasswordInput(attrs={"class": "form-control",
                                                                  "placeholder": "Digite sua senha"}))

    password2 = forms.CharField(label="Confirme sua senha", required=True, max_length=70,
                                widget=forms.PasswordInput(attrs={"class": "form-control",
                                                                  "placeholder": "Digite sua senha novamente"}))

    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get("nome_cadastro")
        if nome:
            nome = nome.strip()
            if " " in nome:
                raise forms.ValidationError("Não é possivel colocar espaço no nome")
            else:
                return nome

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError("Senhas não são iguais")
            else:
                return password2

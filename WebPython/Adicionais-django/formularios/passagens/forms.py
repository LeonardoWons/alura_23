from django import forms
from datetime import datetime
from passagens.validation import *
from tempus_dominus.widgets import DatePicker
from passagens.models import Passagem, ClasseViagem, Pessoa


class PassagemForms(forms.ModelForm):
    data_pesquisa = forms.DateField(label='Data da pesquisa', disabled=True, initial=datetime.today())

    class Meta:
        model = Passagem
        fields = '__all__'  # exibir todos os campos do modelo, pode ser escrito como exclude = [] (nao exclui nada)
        # exclude = ['nome_do_campo_para_excluir']  porem vai mostrar todos os outros que nao forem na lista

        labels = {'data_ida': 'Data de ida'}
        widgets = {
            'data_ida': DatePicker(),
            'data_volta': DatePicker(),
        }

    def clean(self):
        origem = self.clean_data.get('origem')
        destino = self.clean_data.get('destino')
        data_ida = self.cleaned_data.get('data_ida')
        data_volta = self.cleaned_data.get('data_volta')
        data_pesquisa = self.cleaned_data.get('data_pesquisa')
        lista_de_erros = {}

        campo_tem_algum_numero(origem, 'origem', lista_de_erros)
        campo_tem_algum_numero(destino, 'destino', lista_de_erros)
        origem_destino_iguais(origem, destino, lista_de_erros)
        data_ida_maior_que_data_volta(data_ida, data_volta, lista_de_erros)
        data_ida_menor_que_data_pesquisa(data_ida, data_pesquisa, lista_de_erros)

        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro)

        return self.cleaned_data


class PessoaForms(forms.ModelForm):
    class Meta:
        model = Pessoa
        exclude = ['nome']

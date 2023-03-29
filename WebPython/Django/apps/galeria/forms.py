from django import forms
from apps.galeria.models import Fotografia


class FotografiaForms(forms.ModelForm):
    class Meta:
        model = Fotografia
        exclude = ['publicada', ]
        labels = {
            'descricao': 'Descrição',
            'data_fotogradia': 'Data do registro',
            'usuario': 'Usuário'
        }

        widgets = {
            "nome": forms.TextInput(attrs={'class': 'form-control'}),
            "legenda": forms.TextInput(attrs={'class': 'form-control'}),
            "categoria": forms.Select(attrs={'class': 'form-control'}),
            "descrição": forms.Textarea(attrs={'class': 'form-control'}),
            "foto": forms.FileInput(attrs={'class': 'form-control'}),
            "data_fotografia": forms.DateInput(attrs={'class': 'form-control', 'type': 'date'},
                                               format='%d/%m/%Y'),
            "usuario": forms.Select(attrs={'class': 'form-control'}),
        }

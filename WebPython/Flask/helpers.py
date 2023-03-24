import os
from jogoteca import app
from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField, PasswordField


class FormularioJogo(FlaskForm):
    nome = StringField('Nome do Jogo', [validators.DataRequired(), validators.Length(min=1, max=50)])
    categoria = StringField('Categoria', [validators.DataRequired(), validators.Length(min=1, max=40)])
    console = StringField('Console', [validators.DataRequired(), validators.Length(min=1, max=20)])
    salvar = SubmitField('Salvar')


class FormularioUsuario(FlaskForm):
    nickname = StringField('Nickname', [validators.DataRequired(), validators.Length(min=1, max=8)])
    senha = PasswordField('Senha', [validators.DataRequired(), validators.Length(min=1, max=100)])
    login = SubmitField('Login')


def recupera_imagem(id):
    for file_name in os.listdir(app.config['UPLOAD_PATH']):
        if f'capra{id}' in file_name:
            return file_name

    return 'capa_padrao.jpg'


def deleta_arquivo(id):
    file = recupera_imagem(id)
    if file != 'capa_padrao.jpg':
        os.remove(os.path.join(app.config['UPLOAD_PATH'], file))

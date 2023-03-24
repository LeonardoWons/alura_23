from jogoteca import app
from models import Usuarios
from helpers import FormularioUsuario
from flask_bcrypt import check_password_hash
from flask import flash, session, redirect, request, render_template, url_for


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    form = FormularioUsuario()
    return render_template('login.html', proxima=proxima, form=form)


@app.route('/logout')
def logout():
    session['nome_user_logado'] = None
    flash('Logout efetuado com sucesso')
    return redirect(url_for('home_page'))


@app.route('/autenticar', methods=['POST', ])
def aut():
    form = FormularioUsuario(request.form)
    user = form.nickname.data
    proxima_pagina = request.form['proxima']

    usuario = Usuarios.query.filter_by(nickname=user).first()
    senha = check_password_hash(usuario.senha, form.senha.data)

    if usuario and senha:
        session['nome_user_logado'] = usuario.nickname
        flash(f'{user} logado com sucesso.')
        return redirect(proxima_pagina)

    else:
        flash(f'{user} não foi possivel logar.')
        return redirect(url_for('login'))
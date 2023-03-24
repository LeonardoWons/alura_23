from flask import render_template, request, redirect, session, flash, url_for, send_from_directory
from helpers import recupera_imagem, deleta_arquivo, FormularioJogo
from jogoteca import app, db
from models import Jogos
import time


@app.route('/')
def home_page():
    lista = Jogos.query.order_by(Jogos.id)
    return render_template('lista.html', titulo='jogos', jogos=lista)


@app.route('/novo')
def novo():
    if 'nome_user_logado' not in session or session['nome_user_logado'] is None:
        return redirect(url_for('home_page', proxima=url_for('novo')))

    else:
        form = FormularioJogo()
        return render_template('novo.html', titulo='Adicione um novo jogo', form=form)


@app.route('/editar/<int:id>')
def editar(id):
    if 'nome_user_logado' not in session or session['nome_user_logado'] is None:
        return redirect(url_for('home_page', proxima=url_for('editar')))

    else:
        jogo = Jogos.query.filter_by(id=id).first()
        form = FormularioJogo()
        form.nome.data = jogo.nome
        form.categoria.data = jogo.categoria
        form.console.data = jogo.console
        capa_jogo = recupera_imagem(id)
        return render_template('editar.html', titulo='editando jogo', id=id, capa_jogo=capa_jogo, form=form)


@app.route('/criar', methods=['POST', ])
def criar():
    form = FormularioJogo(request.form)

    if not form.validate_on_submit():
        return redirect(url_for('novo'))

    nome = form.nome.data
    catg = form.categoria.data
    plataforma = form.console.data

    jogo = Jogos.query.filter_by(nome=nome).first()

    if jogo:
        flash('O jogo ja existe')
        return redirect(url_for('novo'))

    novo_jogo = Jogos(nome=nome, categoria=catg, console=plataforma)
    db.session.add(novo_jogo)
    db.session.commit()

    file = request.files['arquivo']
    upload_path = app.config['UPLOAD_PATH']
    timestamp = time.time()
    file.save(f'{upload_path}/capa_{novo_jogo.id}_{timestamp}.jpg')

    return redirect(url_for('home_page'))


@app.route('/atualizar', methods=['POST', ])
def atualizar():
    form = FormularioJogo(request.form)

    if form.validate_on_submit():

        jogo = Jogos.query.filter_by(id=request.form['id']).first()
        jogo.nome = form.nome.data
        jogo.categoria = form.categoria.data
        jogo.console = form.console.data

        db.session.add(jogo)
        db.session.commit()

        file = request.files['arquivo']
        upload_path = app.config['UPLOAD_PATH']
        timestamp = time.time()
        deleta_arquivo(jogo.id)
        file.save(f'{upload_path}/capa_{jogo.id}_{timestamp}.jpg')

        flash(f'Jogo {jogo.nome} editado com sucesso')

    return redirect(url_for('home_page'))


@app.route('/deletar/<int:id>')
def deletar(id):
    if 'nome_user_logado' not in session or session['nome_user_logado'] is None:
        return redirect(url_for('login'))

    Jogos.query.filter_by(id=id).delete()
    db.session.commit()
    flash(f'Jogo deletado com sucesso')

    return redirect(url_for('home_page'))


@app.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory('uploads', nome_arquivo)

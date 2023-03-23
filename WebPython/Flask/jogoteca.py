from flask import Flask, render_template, request, redirect, session, flash, url_for


class Jogo:
    def __init__(self, nome, catg, plataforma):
        self.nome = nome
        self.catg = catg
        self.plataforma = plataforma


jogo1 = Jogo('LOL', 'MOBA', 'PC')
jogo2 = Jogo('CS:GO', 'FPS', 'PC')
jogo3 = Jogo('MK5', 'Luta', 'PC/Console')
lista = [jogo1, jogo2, jogo3]


class Usuario:
    def __init__(self, nome, nickname, senha):
        self.nome = nome
        self.nickname = nickname
        self.senha = senha


usuario1 = Usuario("leonardo", "leozen", "1234")
usuario2 = Usuario("livia", "livs", "5678")
usuario3 = Usuario("random", "random_nick", "9999")

usuarios = {
    usuario1.nickname: usuario1,
    usuario2.nickname: usuario2,
    usuario3.nickname: usuario3
}

app = Flask(__name__)
app.secret_key = 'senha_super_secreta'


@app.route('/')
def home_page():
    return render_template('lista.html', titulo='jogos', jogos=lista)


@app.route('/novo')
def novo():

    if 'nome_user_logado' not in session or session['nome_user_logado'] is None:
        return redirect(url_for('home_page', proxima=url_for('novo')))

    else:
        return render_template('novo.html', titulo='Adicione um novo jogo')


@app.route('/criar', methods=['POST', ])
def criar():
    nome = request.form['nome']
    catg = request.form['catg']
    plataforma = request.form['plataforma']
    jogo = Jogo(nome, catg, plataforma)
    lista.append(jogo)
    return redirect(url_for('home_page'))


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)


@app.route('/logout')
def logout():
    session['nome_user_logado'] = None
    flash('Logout efetuado com sucesso')
    return redirect(url_for('home_page'))


@app.route('/autenticar', methods=['POST', ])
def aut():
    user = request.form['usuario']
    senha = request.form['senha']
    proxima_pagina = request.form['proxima']

    if user in usuarios:
        if senha == usuarios[user].senha:
            session['nome_user_logado'] = usuarios[user].nickname
            flash(f'{user} logado com sucesso.')
            return redirect(proxima_pagina)

    else:
        flash(f'{user} não foi possivel logar.')
        return redirect(url_for('login'))


app.run(debug=True)

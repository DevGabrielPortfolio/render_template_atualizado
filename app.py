from flask import Flask, render_template, request, redirect, url_for, session
import random as rd
import os
from model.control_user import Usuario
from data import listas_configuracao
from model.control_mensage import Mensagem
from hashlib import sha256

app = Flask(__name__)

app.secret_key = os.urandom(24)

frasesCadastro = []
coresCadastro = []

@app.route('/')
def paginaCadastro():
    return render_template('index.html')

@app.route('/cadastroUser', methods=['POST'])
def cadastroUser():
    usuario = request.form['nomeCadastro']
    senha = request.form['senhaCadastro']
    senhaCrptografada = sha256(senha.encode()).hexdigest()
    login = request.form['loginUser']

    Usuario.cadastrar_usuario(login, usuario, senhaCrptografada)
    return redirect('/home')

@app.route('/login', methods=['POST'])
def login():
    user = request.form['nomeLogin']
    senha = request.form['senhaLogin']
    senhaCriptografadaLogin = sha256(senha.encode()).hexdigest()

    Usuario.validar_login(user, senhaCriptografadaLogin)
    return redirect('/home')

@app.route('/home')
def home():
    curiosidade = rd.choice(listas_configuracao.curiosidades_basquete)
    cor = rd.choice(listas_configuracao.cores_fundo)
    imagem = rd.choice(listas_configuracao.lista_imagens)

    return render_template('home.html', texto_curiosidade=curiosidade, imagem=imagem, cor_fundo=cor)

@app.route('/curiosidades')
def primeiroweb():
    # Escolhendo curiosidade, cor e imagem
    curiosidade = rd.choice(listas_configuracao.curiosidades_basquete)
    cor = rd.choice(listas_configuracao.cores_fundo)
    imagem = rd.choice(listas_configuracao.lista_imagens)

    return render_template('home.html', texto_curiosidade=curiosidade, imagem=imagem, cor_fundo=cor)

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html', itens=frasesCadastro)

@app.route('/comentarios')
def comentarios():
    mensagens = Mensagem.recuperar_mensagems()
    return render_template("comentarios.html", mensagens=mensagens)

@app.route("/post/cadastrarmensagem", methods = ["POST"])
def post_mensagem():
    # Peguei as informações vinda do usuário
    usuario = request.form.get("usuario")
    comentario = request.form.get("comentario")

    # Cadastrando a mensagem usando a classe Mensagem 
    Mensagem.cadastrar_mensagem(usuario, comentario)
    
    # Rediriciona para o index
    return redirect("/comentarios")

@app.route('/receber', methods=['POST'])
def receber():
    frase = request.form['nome']
    if(frase.lower() == 'clear'):
        frasesCadastro.clear()
    else:
        frasesCadastro.append(frase)

    return redirect(url_for('cadastro'))

@app.route('/cadastroCor')
def cadastroCor():
    return render_template('cadastro-cor.html', itens=coresCadastro)

@app.route('/receberCor', methods=['POST'])
def receberCor():
    corNome = request.form['nomeCor']
    if(corNome.lower() == 'clear'):
        coresCadastro.clear()
    else:
        coresCadastro.append(corNome)
        

    return redirect(url_for('cadastroCor'))

@app.route('/excluirCor/<cor>', methods=['POST'])
def excluirCor(cor):
    if cor in coresCadastro:
        coresCadastro.remove(cor)
    return redirect(url_for('cadastroCor'))

@app.route('/deleteComentario/mensagem/<codigo>')
def delete_mensagem(codigo):
    Mensagem.delete_message(codigo)
    return redirect('/comentarios')

@app.route('/like/mesagem/<codigo>')
def like_mensagem(codigo):
    Mensagem.add_like(codigo)
    return redirect('/comentarios')

@app.route('/deslike/mensagem/<codigo>')
def deslike_mensagem(codigo):
    Mensagem.add_dislike(codigo)
    return redirect('/comentarios')

# Executa o app
if __name__ == '__main__':
    app.run(debug=True)
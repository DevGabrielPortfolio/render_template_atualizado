import datetime
from flask import session
from data.conexao import Conexao, ConexaoLocal

class Usuario:
    def cadastrar_usuario(login, user, password):

        conn = Conexao.criar_conexao()

        cursor = conn.cursor()

        sql = "INSERT INTO tb_usuarios (login, nome, senha) VALUES (%s,%s, %s)"

        valores = (login, user, password)

        cursor.execute(sql, valores)

        conn.commit()

        cursor.close()
        conn.close()


    def validar_login(login, password):

        conn = Conexao.criar_conexao()

        cursor = conn.cursor(dictionary=True)

        sql = "SELECT nome, login, senha FROM tb_usuarios WHERE login = %s AND senha = %s"

        valores = (login, password)

        cursor.execute(sql, valores)

        resultado = cursor.fetchone()

        cursor.close()
        conn.close()

        if resultado:
            session['usuario'] = resultado['login']
            session['nome_usuario'] = resultado['nome']
            return True
        else:
            return False


    def logoff():
        session.clear()
import datetime
from data.conexao import Conexao, ConexaoLocal

class Usuario:
    def cadastrar_usuario(user, password):

        conn = ConexaoLocal.criar_conexao()

        cursor = conn.cursor()

        sql = "INSERT INTO usuarios (nome, senha) VALUES (%s,%s)"

        valores = (user, password)

        cursor.execute(sql, valores)

        conn.commit()

        cursor.close()
        conn.close()


    def validar_login(user, password):

        conn = ConexaoLocal.criar_conexao()

        cursor = conn.cursor()

        sql = "SELECT COUNT(*) FROM usuarios WHERE nome = %s AND senha = %s"

        valores = (user, password)

        cursor.execute(sql, valores)

        resultado = cursor.fetchone()

        cursor.close()
        conn.close()

        if resultado[0] > 0:
            return True
        else:
            return False

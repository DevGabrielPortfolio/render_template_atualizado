import datetime
from data.conexao import Conexao 
from mysql.connector import Error

class Mensagem:
    
    def  cadastrar_mensagem(usuario, comentario):

        data_hora_comentario = datetime.datetime.today()
   
   
        # Criando a conexão com o banco de dados
        conexao = Conexao.criar_conexao()

        # O cursor será responsável por manipular
        cursor = conexao.cursor()

        # Criando o sql que será executado
        sql = """INSERT INTO tb_comentarios
                    (nome, data_hora, comentario)
                VALUES
                    (%s, %s, %s)"""
                
        valores = (usuario, data_hora_comentario, comentario)
    
        # Executando o comnado sql
        cursor.execute(sql,valores)
    
        # Confirmo a alteração (commit serve para fixar a alteração)
        conexao.commit()
    
        # Fecho a conexao com o banco
        cursor.close()
        conexao.close()

    def recuperar_mensagems():

        #Criar conexão 
        conexao = Conexao.criar_conexao()

        # O cursor será responsável por manipular
        cursor = conexao.cursor(dictionary = True)

        # Criando o sql que será executado
        sql = "SELECT cod_comentario, curtidas, nome AS usuario, comentario, data_hora FROM tb_comentarios;"

        #Executando o comando sql
        cursor.execute(sql)        

        #Recuperando os dados e jogando em uma varialvel 
        resultado = cursor.fetchall()

        #Fecho a conexão (como não ouve alteração não preciso do commit)
        conexao.close()

        return resultado
    
    def delete_message(id):
        # Criando a conexão com o banco de dados
        conexao = Conexao.criar_conexao()

        # O cursor será responsável por manipular
        cursor = conexao.cursor()

        # Criando o sql que será executado
        sql = """DELETE FROM tb_comentarios WHERE cod_comentario = %s;"""
                
        valores = (id,)
    
        # Executando o comnado sql
        cursor.execute(sql,valores)
    
        # Confirmo a alteração (commit serve para fixar a alteração)
        conexao.commit()
    
        # Fecho a conexao com o banco
        cursor.close()
        conexao.close()
    
    def add_like(id):
        # Criando a conexão com o banco de dados
        conexao = Conexao.criar_conexao()

        # O cursor será responsável por manipular
        cursor = conexao.cursor()

        # Criando o SQL que será executado
        sql = """UPDATE tb_comentarios
                SET curtidas = curtidas + 1
                WHERE cod_comentario = %s;"""

        valores = (id,)
        
        # Executando o comando SQL
        cursor.execute(sql, valores)
        
        # Confirmo a alteração (commit serve para fixar a alteração)
        conexao.commit()
        
        # Fecho a conexão com o banco
        cursor.close()
        conexao.close()

    def add_dislike(id):
        # Criando a conexão com o banco de dados
        conexao = Conexao.criar_conexao()

        # O cursor será responsável por manipular
        cursor = conexao.cursor()

        # Criando o SQL que será executado
        sql = """UPDATE tb_comentarios
                SET curtidas = curtidas - 1
                WHERE cod_comentario = %s;"""

        valores = (id,)
        
        # Executando o comando SQL
        cursor.execute(sql, valores)
        
        # Confirmo a alteração (commit serve para fixar a alteração)
        conexao.commit()
        
        # Fecho a conexão com o banco
        cursor.close()
        conexao.close()
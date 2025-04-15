import datetime
from data.conexao import Conexao, ConexaoLocal
from mysql.connector import Error

class Mensagem:
    
    def  cadastrar_mensagem(usuario, comentario):

        data_hora_comentario = datetime.datetime.today()
   
   
        # Criando a conexão com o banco de dados
        conn = Conexao.criar_conexao()

        # O cursor será responsável por manipular
        cursor = conn.cursor()

        # Criando o sql que será executado
        sql = """INSERT INTO tb_comentarios
                    (nome, data_hora, comentario)
                VALUES
                    (%s, %s, %s)"""
                
        valores = (usuario, data_hora_comentario, comentario)
    
        # Executando o comnado sql
        cursor.execute(sql,valores)
    
        # Confirmo a alteração (commit serve para fixar a alteração)
        conn.commit()
    
        # Fecho a conexao com o banco
        cursor.close()
        conn.close()

    def recuperar_mensagems():

        #Criar conexão 
        conn = Conexao.criar_conexao()

        # O cursor será responsável por manipular
        cursor = conn.cursor(dictionary = True)

        # Criando o sql que será executado
        sql = "SELECT cod_comentario, curtidas, nome AS usuario, comentario, data_hora FROM tb_comentarios;"

        #Executando o comando sql
        cursor.execute(sql)        

        #Recuperando os dados e jogando em uma varialvel 
        resultado = cursor.fetchall()

        #Fecho a conexão (como não ouve alteração não preciso do commit)
        conn.close()

        return resultado
    
    def delete_message(id):
        # Criando a conexão com o banco de dados
        conn = Conexao.criar_conexao()

        # O cursor será responsável por manipular
        cursor = conn.cursor()

        # Criando o sql que será executado
        sql = """DELETE FROM tb_comentarios WHERE cod_comentario = %s;"""
                
        valores = (id,)
    
        # Executando o comnado sql
        cursor.execute(sql,valores)
    
        # Confirmo a alteração (commit serve para fixar a alteração)
        conn.commit()
    
        # Fecho a conexao com o banco
        cursor.close()
        conn.close()
    
    def add_like(id):
        # Criando a conexão com o banco de dados
        conn = Conexao.criar_conexao()
        cursor = conn.cursor()

        # Criando o SQL que será executado
        sql = """UPDATE tb_comentarios
                SET curtidas = GREATEST(0, curtidas + 1)
                WHERE cod_comentario = %s;"""

        valores = (id,)

        # Executando o comando SQL
        cursor.execute(sql, valores)
        conn.commit()

        # Fechando a conexão
        cursor.close()
        conn.close()


    def add_dislike(id):
        # Criando a conexão com o banco de dados
        conn = Conexao.criar_conexao()
        cursor = conn.cursor()

        # Criando o SQL que será executado
        sql = """UPDATE tb_comentarios
                SET curtidas = GREATEST(curtidas - 1, 0)
                WHERE cod_comentario = %s;"""

        valores = (id,)

        # Executando o comando SQL
        cursor.execute(sql, valores)
        conn.commit()

        # Fechando a conexão
        cursor.close()
        conn.close()


    def ultimaMensagem(usuario):
        conn = Conexao.criar_conexao()
        cursor = conn.cursor()

        sql = """
            SELECT comentario 
            FROM tb_comentarios 
            WHERE nome = %s 
            ORDER BY cod_comentario DESC 
            LIMIT 1;
        """
        cursor.execute(sql, (usuario,))
        
        resultado = cursor.fetchone()

        cursor.close()
        conn.close()

        if resultado:
            return resultado[0]
        else:
            return "Nenhuma mensagem encontrada"

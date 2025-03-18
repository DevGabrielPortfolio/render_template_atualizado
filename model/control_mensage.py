import datetime
from data.conexao import Conexao 

class Mensagem:
    
    def  cadastrar_mensagem(usuario, comentario):

        data_hora = datetime.datetime.today()
   
   
        # Criando a conexão com o banco de dados
        conexao = Conexao.criar_conexao()

        # O cursor será responsável por manipular
        cursor = conexao.cursor()

        # Criando o sql que será executado
        sql = """INSERT INTO tbComentario
                    (nome, data_comentario, comentario)
                VALUES
                    (%s, %s, %s)"""
                
        valores = (usuario, data_hora, comentario)
    
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
        sql = "SELECT nome AS usuario, comentario, data_comentario FROM tbComentario;"

        #Executando o comando sql
        cursor.execute(sql)        

        #Recuperando os dados e jogando em uma varialvel 
        resultado = cursor.fetchall()

        #Fecho a conexão (como não ouve alteração não preciso do commit)
        conexao.close()

        return resultado
    
import mysql.connector

class Conexao:
    
    def criar_conexao():
        # Criando a conexão com o banco de dados local
        # conexao = mysql.connector.connect(host = "localhost",
        #                                 port = 3306,
        #                                 user = "3ds",
        #                                 password = "banana",
        #                                 database = "db_feedback")

        # Criando a conexão com o banco de dados na nuvem
        conexao = mysql.connector.connect(host = "bdgodofredo-alexstocco-93db.b.aivencloud.com",
                                        port = 27974,
                                        user = "3ds",
                                        password = "banana",
                                        database = "db_feedback")
        
        return conexao
    

class ConexaoLocal:    
    def criar_conexao():
        # Criando a conexão com o banco de dados
        conexao = mysql.connector.connect(host = "localhost",
                                        port = 3306,
                                        user = "root",
                                        password = "root",
                                        database = "dbFeedback")
        
        return conexao
import sqlite3

db = "database/projeto.sqlite3"
#Função que solicita informação do banco de dados.
def dataBaseConsult(query):
    connect = sqlite3.connect(db)
    cursor = connect.cursor()
    execute = cursor.execute(query)
    result = execute.fetchall()
    connect.close()
    return result
#Função que alimenta o banco com informações.
def dataBaseInsert(query):
    connect = sqlite3.connect(db)
    cursor = connect.cursor()
    cursor.execute(query)
    connect.commit()
    connect.close()
    return
    
    




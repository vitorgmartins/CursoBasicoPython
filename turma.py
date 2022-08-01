import db
# Estrutura da turma = {id,nome}
turmas = {}

def carregarTurmas():
    query = ("select * from turma;")
    result = db.dataBaseConsult(query)
    return result
turmas = carregarTurmas()

def validaTurma(turma,id):
    if turma == []:
        query = ("select * from turma where turma_id ="+ str(id) + ";")
        turma = db.dataBaseConsult(query)
        if turma == []:
            print("A turma em questão não existe no sistema.")
            return False
        else:
            print("A turma existe, porém não há alunos cadastrados.")
            return True
    else:
        #print(result)
        return True

def listarTurmas():
    for turma in turmas:
        query = ("select count(*) from aluno where turma_id ="+str(turma[0])+";")
        result = db.dataBaseConsult(query)
        print("ID: "+str(turma[0])+" | Qtd: "+str(result[0][0])+" | Nome:"+str(turma[1]))
        pass
    print("\n")
    pass
#listarTurmas()

def listarTurma(id):
   
    try:
      id = int(id)
    except ValueError:
        print("Você digitou "+ str(id)+",\n o programa espera que você digite um número inteiro. \n Tente Novamente.")
        return

    query = ("select * from aluno where turma_id ="+str(id)+";")
    turma = db.dataBaseConsult(query)

    query = ("select turma_nome from turma where turma_id ="+str(id)+";")
    turmaNome = db.dataBaseConsult(query)
    try:
        print("Turma Nome: "+str(turmaNome[0][0]))
    except IndexError:
        print("Turma não existe!")
        pass
    validaTurma(turma,id)

    for aluno in turma:
        print("ID: "+str(aluno[0])+" | Nome: "+str(aluno[1]))
        pass
    return turma 
#listarTurma(10)

# Refatorar para testar se a turma existe.
def cadastrarTurmas():
    nomeTurma = input("Digite um codigo/nome para a turma:\n")
    query = ("INSERT INTO turma (turma_nome) VALUES ('"+ str(nomeTurma) +"')")
    db.dataBaseInsert(query)
    pass




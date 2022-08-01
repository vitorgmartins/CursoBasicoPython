import db 
import turma 

def listarTodosAlunos():
    query = ("select * from aluno;")
    alunos = db.dataBaseConsult(query)
    return alunos

def cadastrarAluno():
    print("-{ \nIniciando Cadastro - Aluno}-")
    nomeCompleto = input("::Insira o nome completo do aluno:\n")
    print("Q: em qual turma deseja cadastrar o aluno?\n Seleciona o ID turma a baixo:\n")
    turma.listarTurmas()
    idTurma = input ("::Insira o ID da turma desejada:\n")

    if turma.validaTurma([],idTurma) == False:
        return

    query = ("INSERT INTO aluno (aluno_nome,turma_id) VALUES ('"+str(nomeCompleto)+"',"+str(idTurma)+");")
    db.dataBaseInsert(query)
    print("!!! - Aluno Cadastrado - !!!")
    pass

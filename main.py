import os
import db
import turma
import alunos

try:
    os.mkdir("projeto/turmas",mode=0o777, dir_fd=None)
except FileExistsError:
    print("Pasta já existe")
    pass
except FileNotFoundError:
    print("Arquivo não encontrado")
    pass

controle = True

def menu():
# Programa de uma escola para cadastrar turmas e alunos no sistema.
    print("=============")
    print("   Escola    ")
    print("=============")
    print("  -= Menu =- ")
    print("Opções:")
    print("1 - Cadastrar Turmas ")
    print("2 - Exibir turmas ")
    print("3 - Inspecionar turma ")
    print("4 - Listar Alunos   ")
    print("5 - Cadastrar Alunos ")
    print("0 - Sair")
    print("=============")
    pass


while controle == True:
    menu()
    #variável opção recebe a opção que o usuário seleciona no sistema
    opcao = int(input("Insira a opção:\n"))

    match(opcao):
        #o case executa a saída do sistema
        case(0):
            print("Saindo...")
            controle = False
        # Se você desejar cadastrar turmas, escolha a opção um para criar turma e posteriormente insira a quantidade almejada. 
        case(1):
            turma.cadastrarTurmas()
        case(2): 
            turma.listarTurmas()
        case(3):
            turma.listarTurma(input("Insira o id da turma:\n"))
        case(4):
            print(alunos.listarTodosAlunos())

            for aluno in alunos:
                print("NOME:"+str(aluno[1])+"TURMA:"+str(aluno[2]))
                pass
        case(5):
            alunos.cadastrarAluno()
    pass

print("fim da execução")
 


     


    


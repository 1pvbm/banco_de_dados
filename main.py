import mysql.connector
from prettytable import PrettyTable
class conexaoBD:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='118411',
            database='Academia',
        )
        self.cursor = self.conexao.cursor()
    def exit_conexao(self):
        self.cursor.close()
        self.conexao.close()
class acaoesBd:
    def __init__(self, conexao, cursor):
        self.conexao = conexao
        self.cursor = cursor
    def play_comando(self, comando):
        self.cursor.execute(comando)
        self.conexao.commit()

    def shere_dados(self, comando):
        self.cursor.execute(comando)
        return self.cursor.fetchall()
        tupla = self.cursor.fetchall()

        list = [list(i) for i in tupla]

        tabela = PrettyTable()
        tabela.field_names = ['nome', 'cpf']
        for row in list:
            tabela.add_row(row)

        return tabela


def show_menu():
    print("Escolha uma opção:")
    print("1. create")
    print("2. delete")
    print("3. read")
    print("4. update")
    print("5. Sair\n")


conexao = conexaoBD()
operacoes = acaoesBd(conexao.conexao, conexao.cursor)
while True:
    show_menu()
    opcao = input("Digite o número da opção desejada: [1 à 5 ]: ")

    if opcao == "1":  # CREATE
        nome_aluno_novo = input("Digite o nome do Aluno: ")
        cpf_novo = input("Digite o CPF do aluno: ")
        comando_um = (f'INSERT INTO aluno (nome, cpf) VALUES ('
                          f'"{nome_aluno_novo}", '
                          f'"{cpf_novo}")')
        operacoes.play_comando(comando_um)
        
    elif opcao == "2":  # DELETE
        nome_aluno_del = input("Digite o nome do aluno: ")
        comando_dois = f'DELETE FROM aluno WHERE nome = "{nome_aluno_del}"'
        matricula_aluno_delete = input("Digite a matricula do aluno a ser removido: ")
        comando_matricula = f'DELETE FROM alunos WHERE matricula = "{matricula_aluno_delete}"'
        operacoes.play_comando(comando_matricula)

    elif opcao == "3":  # READ
        comando_tres = 'SELECT * FROM aluno'
        result = operacoes.shere_dados(comando_tres)
        print(result)

    elif opcao == "4":  # UPDATE
        nome_aluno = input("Digite o novo nome do aluno para atualizar: ")
        cpf_up = input("Digite o cpf do aluno: ")
        comando_up = f'UPDATE aluno SET nome = {nome_aluno} WHERE cpf = "{cpf_up}"'
        operacoes.play_comando(comando_up)

    elif opcao == "5":  # Sair
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
        continue
conexao.exit_conexao()

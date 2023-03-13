import datetime
from cliente import Cliente
from funcionario import Funcionario


class Cadastros():
    def __init__(self):
        self.anoHoje = datetime.date.today().year
    
    def cliente(self):
        nome = input("Informe o nome do cliente: ")
        cpf = input("Informe o CPF: ")
        email = input("Informe o e-mail: ")
        telefone = input("Informe o telefone: ")
        anoNascimento = int(input("Informe o Ano de nascimento: "))
        
        clienteObj = Cliente(nome, email, cpf, telefone)

        clienteObj.exibir()
        clienteObj.verificaMaiorIdade(anoNascimento, self.anoHoje)
        
    def funcionario(self): 
        nome = input("Informe o nome do funcionario: ")
        cpf = input("Informe o CPF: ")
        email = input("Informe o e-mail: ")
        telefone = input("Informe o telefone: ")
        anoNascimento = int(input("Informe o Ano de nascimento: "))
        cargo = input("Informe o Cargo: ")
        salario = input("Informe o Salario: ")
        
        funcionarioObj = Funcionario(nome, email, cpf, telefone, salario, cargo)
        
        funcionarioObj.exibir()
        funcionarioObj.verificaMaiorIdade(anoNascimento, self.anoHoje)
        
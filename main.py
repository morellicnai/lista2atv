import datetime
from cliente import cliente

nome = input("Informe o nome do cliente: ")
cpf = input("Informe o CPF: ")
email = input("Informe o email: ")
telefone = input("informe o telefone: ")
anoNacimento = int(input ("Informe o ano de nacimento: "))

clienteOBj = cliente(nome, email, cpf, telefone)

clienteOBj.exibir()

clienteOBj.verificamaiordeidade(anoNacimento, datetime.date.today().year)






























































































































































































































































































































































































































































































































































































































































































































































































































































































































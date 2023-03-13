class Funcionario():
    
    def _init_(self, nome, cpf, email, telefone, cargo, salario):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.telefone = telefone
        self.cargo = cargo
        self.salario = salario

    def exibir(self):
        print ("\nO nome do cliente é " + self.nome)
        print ("O E-mail é " + self.email)
        print ("O CPF é " + self.cpf)
        print ("O telefone é " + self.telefone)
        print ("O cargo é " + self.cargo)
        print ("O salario é " + self.salario)
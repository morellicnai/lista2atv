class Cliente():
    def __init__(self, nome, email, cpf, telefone):
        self.nome = nome
        self.email = email
        self.cpf = cpf 
        self.telefone = telefone
        
    def exibir(self):
        print("O nome do cliente é " + self.nome)
        print("O email é " + self.email)
        print("O CPF é " + self.cpf)
        print("O Telefone é " + self.telefone)
        
    def verificaMaiorIdade(self, anoNascimento, anoHj):
        idade = anoHj - anoNascimento
        if idade >= 18:
            print("É maior de idade")
        else: 
            print("É menor")
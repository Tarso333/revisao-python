class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade =  idade

    def apresentar(self):
        print(f'Olá, meu nome é {self.nome}, e tenho {self.idade} anos de idade! ')    


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo):
        super().__init__(nome, idade) #função embutida para chamar as informações necessárias da função principal
        self.cargo = cargo

    def trabalhar(self):    
        print(f'{self.nome} está trabalhando como {self.cargo}!\n')

class Cliente(Pessoa):
    def __init__(self, nome, idade, saldo):
        super().__init__(nome, idade)
        self. saldo =  saldo

    def extrato(self):
        print(f'{self.nome} possui em sua conta {self.saldo} reais de saldo! ') 
           
f1 = Funcionario ('Maria', 38, 'Analista Senior')
f1.apresentar()
f1.trabalhar()

c1 = Cliente('Tarso', 21, '50.000$')
c1.apresentar()
c1.extrato()
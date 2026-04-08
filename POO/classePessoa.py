class Pessoa: #classe
    
    def __init__(self, nome, idade, sexo, cargo): #construtor 
        self.nome = nome
        self.idade = idade
        self.sexo =  sexo
        self.cargo = cargo

    def apresentar(self): #metódo
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")   
        print(f"Sexo: {self.sexo}")
        print(f"Cargo: {self.cargo}")

    def promover(self, novo_cargo):

        print(f'{self.nome} foi promovido(a) para a nova funcão de {novo_cargo}')
        self.cargo =  novo_cargo

    def atualizar_idade (self, nova_idade):
        if nova_idade > self.idade:
            print(f'Atualizando a idade de {self.idade} para {nova_idade}')
        else:
            print('A nova idade tem que ser maior que a antiga')
        self.idade = nova_idade

        print('\nPessoa 1 ') #instância
p1 = Pessoa("Tarso", 21, 'M', 'Estagiário')
p1.promover('Analista Pleno')
p1.atualizar_idade(32)
p1.apresentar()

print('\nPessoa 2 ')
p2 = Pessoa("Ana", 29, 'F', 'Prestadora')
p2.apresentar()

print('\nPessoa 3')
p3 = Pessoa("Salenko", 24, 'M', 'Analista de TI')
p3.apresentar()

print('\nPessoa 4')
p4 = Pessoa("Hallana", 21, 'F', 'Estágiario')
p4.apresentar()
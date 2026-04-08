class Animal:

    def __init__(self, nome, cor, especie):

        self.nome = nome
        self.cor = cor
        self.especie = especie

    def apresentar(self):
        print(f'Eu sou o {self.especie} chamado {self.nome}')

class Animal2:
    def __init__(self, porte, sexo, origem):
        
        self.porte = porte
        self.sexo = sexo
        self.origem = origem

    def informacoes(self):
        print(f'Sou um animal de {self.porte} porte, sou um {self.sexo}, e sou um animal de origem {self.origem}')


class Gato(Animal):
    def emitir_som(self):
        print('Miau!')
        

class Cachorro(Animal, Animal2):
    def __init__(self, nome, cor, especie, porte, sexo, origem):
        Animal.__init__(self, nome, cor, especie)
        Animal2.__init__(self, porte, sexo, origem)

cachorro1 = Cachorro('Russo', 'Preto', 'Pastor Alemão', 'Grande', 'Macho', 'Alemã')

cachorro1.apresentar()
cachorro1.informacoes()      

class Elefante(Animal):
    pass

elefante1 = Elefante('Zeca', 'Azul', 'Africano')
elefante1.apresentar()

gato1 = Gato('Felix', 'Branco','Siamese')
gato1.emitir_som()
            
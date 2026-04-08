#Herança Multinivel

#Classe Avô

class Animal:  
    def __init__(self, nome):
        self.nome = nome

#Classes Pai
class Predador(Animal):
    def cacando(self):
        print(f'O animal {self.nome} animal está caçando!')

class Presa(Animal):
    def fugindo(self):
        print(f'O animal {self.nome} está fugindo!')

#Classes Filho
class Coelho(Presa):
    pass

class Tigre (Predador):
    pass

class Golfinho(Predador, Presa): #Herança Multipla
    pass

coelho1 = Coelho('Bunny')
coelho1.fugindo()

tigre1 = Tigre('Joca')
tigre1.cacando()

golfinho1 = Golfinho('Billie')
golfinho1.cacando()



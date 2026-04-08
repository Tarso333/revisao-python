#Polymorphism

class Personagens():
    def falar(self):
        print('Personagem: Olá, eu sou um personagem!')

class Guerreiro(Personagens):
    def falar(self):
        print('Guerreiro: Olá, eu sou um guerreiro!')
 
class Mago(Personagens):
    def falar(self):
        print('Mago: Olá, eu sou um mago!')

class Guerreiro(Personagens):
    def falar(self):
        print('Guerreiro: Olá, eu sou um guerreiro!')

class Arqueiro(Personagens):
    def falar(self):
        print('Arqueiro: Olá, eu sou um arqueiro!')


#Criando objetos

personagens = [Guerreiro(), Mago(), Arqueiro()]

for p in personagens:
    p.falar()
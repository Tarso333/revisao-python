# Herança Múltipla

#Classes Pai
class Predador():
    def cacando(self):
        print('Este animal está caçando!')

class Presa():
    def fugindo(self):
        print('Este animal está sendo caçado!')

#Classes Filho
class Coelho(Presa):
    pass

class Tigre (Predador):
    pass

class Golfinho(Predador, Presa): #Herança Multipla
    pass

coelho1 = Coelho()
coelho1.fugindo()

tigre1 = Tigre()
tigre1.cacando()

golfinho1 = Golfinho()
golfinho1.cacando()


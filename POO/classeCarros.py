class Carro: # classe
    def __init__(self, cor, ano, modelo): #construtor
        self.cor = cor
        self.ano =  ano
        self.modelo = modelo
        self.ligado = True 
        self.seta = None
        

    def informacoes(self): #metodo
        print(f'Carro {self.modelo} | Ano: {self.ano} | Cor: {self.cor}')
    
    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print('O carro foi ligado')
        else:
            print('O carro já estava ligado')

    def desligar(self):
        if self.ligado:
            self.ligado = False
            print('O carro foi desligado')
        else:
            print('O carro estava desligado')    

    def ligar_seta(self, direcao):
        if not self.ligado:
            print('Ligue o carro primeiro!')
            return   

        self.seta = direcao
        print(f'Seta ligada para a {self.seta}')


print('\nCarro 1: ')
c1 = Carro('Branco', 2022, 'SUV')
c1.informacoes()
c1.ligar()
c1.ligar_seta('esquerda')
class Motor:
    def __init__(self, marca, potencia):
        self.marca = marca
        self.potencia = potencia

class Carro:
    def __init__(self):
        self.motores = []
    def adicionar_motor(self, motor):
        self.motores.append(motor)

    def listar_motores(self):
        for motor in self.motores:
            print(f'Marca: {motor.marca}, Potência: {motor.potencia} cavalos')    

# Criando motores

motor_v6 = Motor ('Ford', 300)
motor_v8 = Motor ('Chevrolet', 400)
motor_v12 = Motor ('Ferrari', 700)
motor_v14 = Motor ('Lamborghini', 1200)
#Criando carro e adicionando motor
carro = Carro()
carro.adicionar_motor(motor_v6)
carro.adicionar_motor(motor_v8) 
carro.adicionar_motor(motor_v12)
carro.adicionar_motor(motor_v14)

# Listando motores do carro
carro.listar_motores()

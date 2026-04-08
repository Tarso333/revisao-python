# Calculadora de IMC - Índice de Massa Corporal

altura = int(input('Informe sua altura em CM: '))
peso = float(input('Informe o seu peso em quilogramas: '))

# Convertendo altura para metros
altura_m = altura / 100

# Cálculo correto do IMC
imc = peso / (altura_m ** 2)

print(f'Seu IMC é: {imc:.2f}')

if imc <= 0:
    print('Valor inválido!')
elif imc <= 18.5:
    print('Magreza')
elif imc <= 24.9:
    print('Normal')
elif imc <= 29.9:
    print('Sobrepeso')
elif imc <= 39.9:
    print('Obesidade')
else:
    print('Obesidade grave')
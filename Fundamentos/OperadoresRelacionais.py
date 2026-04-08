#Igual ou maior que 18 anos de idade é

idade = int(input('Informe a sua idade: '))
cnh = input('Você possui CNH? [Y/N] ')

   

if idade >= 18 and cnh == 'Y':
    print('Você pode dirigir um veículo!')

elif idade >= 18 and cnh == 'N':
    print('Você é maior de idade, mas não possui CNH.')

else:
    print('Você é menor de idade e não pode ter CNH.')

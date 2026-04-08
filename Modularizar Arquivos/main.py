# main.py
from funções import verificar_maioridade

idade = int(input('Digite sua idade: '))

if verificar_maioridade(idade):
    print('Você é maior de idade :)')
else:
    print('Você é menor de idade')  
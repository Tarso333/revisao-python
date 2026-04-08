#Desafio com funções

'''
Criar um programa que calcula a quantidade de tinta necessário para pintar uma parede. O usuário deverá fornecer as seguintes 
informações: Rendimento, altura e largura.
O programa deve mostrar na tela a mensagem 'Você necessita de x latas de tinta'
'''

import math

#entrada dos dados fornecidos pelo usuário
altura = float(input('Informe a altura da parede (m):'))
largura = float(input('Informe a largura da parede (m): '))
rendimento = float(input('Informe o rendimento da tinta (m² por lata): '))

#formula da área
area = altura * largura

#calculo da quantiade de latas (arredodando sempre pra cima)
latas = math.ceil(area / rendimento)

#saída
print(f'Você necessita de {latas} latas de tinta')
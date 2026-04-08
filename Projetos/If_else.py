'''
Criar um programa que dependendo da temperatura (em celsius) do steak
ele retorna o ponto de cozimento em portugues. O usuario deverá 
fornecer a temperatura.

Temperaturas - Cozimento
120°F ou 48°C - Rare (Selada) 
130°F ou 54°C - Medium Rare (Ao ponto para o mal) 
140°F ou 60°C - Medium (Ao ponto) 
150°F ou 65°C - Medium Well (Ao ponto pra o bem) 
160°F ou 71°C - Well done(Bem passada) 
'''

temperatura = int(input('Informe a temperatura da carne: [Graus Celsius] '))

if temperatura < 0:
    print('Temperatura inválida')
    
elif temperatura <= 48:
    print('A carne ainda está crua, cozinhe mais um pouco! ')
elif  temperatura <= 54:
    print('A carne já está selada! ')
elif  temperatura <= 60:
    print('A carne está ao ponto para mal! ')
elif  temperatura <= 65:
    print('A carne está ao ponto!')
elif  temperatura <= 71:
    print('A carne está ao ponto para bem!')
else :
    print('A carne está bem passada')

    
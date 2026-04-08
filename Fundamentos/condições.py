idade = int(input('Qual é a sua idade? '))
autorizacao_dos_pais = input('Tem autorização dos pais? (s/n):')

if idade >=18:
    print('Acesso ao sistema liberado!')

elif idade >=16 and autorizacao_dos_pais == 's':
    print('Acesso ao sistema liberado via autorizacao')

else:
    print('Acesso Negado!')
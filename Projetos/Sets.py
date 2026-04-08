#Desafio com sets


funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa']
turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
turno_noite = ['Pedro', 'Sophia', 'Bruno']
tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']

# Convertendo listas para sets
funcionarios_set = set(funcionarios)
dia_set = set(turno_dia)
noite_set = set(turno_noite)
carro_set = set(tem_carro)

# Lista 1: Tem carro e trabalham à noite
lista1 = carro_set & noite_set

# Lista 2: Tem carro e trabalham de dia
lista2 = carro_set & dia_set

# Lista 3: Não têm carro
lista3 = funcionarios_set - carro_set

# Exibindo resultados
print("Lista 1 (Carro + Noite):", lista1)
print("Lista 2 (Carro + Dia):", lista2)
print("Lista 3 (Sem Carro):", lista3)
produtoEstoque = int(input('Digite quantas unidades do produto tem estoque: '))
qtdUsadasDia = int(input('Informe quantas unidades é usada por dia: '))

duracaoProduto = produtoEstoque / qtdUsadasDia

print(f'\nNo estoque possui {produtoEstoque} unidades do produto')
print(f'A quantidade usadas por dia é {qtdUsadasDia} unidades do produto')
print(f'Logo, o produto em estoque durará {duracaoProduto:.1f} dias.')


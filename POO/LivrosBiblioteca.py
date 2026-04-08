class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor


class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def listar_livros(self):
        if not self.livros:
            print("A biblioteca está vazia.")
        else:
            for livro in self.livros:
                print(f'Título: {livro.titulo}, Autor: {livro.autor}')

    def buscar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                return livro
        return None


# Criando livros
livro1 = Livro('Dom Casmurro', 'Machado de Assis')
livro2 = Livro('1984', 'George Orwell')
livro3 = Livro('O Hobbit', 'J.R.R. Tolkien')
livro4 = Livro('O vinho novo é melhor', 'Luciano Subirá')

# Criando biblioteca
biblioteca = Biblioteca()

# Adicionando livros
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)
biblioteca.adicionar_livro(livro4)

# Listando livros
print(" Lista de livros:")
biblioteca.listar_livros()

# Buscando um livro
print("\n Buscando livro:")
titulo_busca = 'O vinho novo é melhor'
resultado = biblioteca.buscar_livro(titulo_busca)

if resultado:
    print(f'Livro encontrado: {resultado.titulo} - {resultado.autor}')
else:
    print("Livro não encontrado.")
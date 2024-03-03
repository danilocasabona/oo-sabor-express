from desafio6 import Livro

# 6. No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.

livro4 = Livro('O Senhor dos Anéis', 'J.R.R. Tolkien', 1954)
livro4.emprestar()
print(livro4.disponivel)

# 7. No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.
ano = 1954
livros_disponiveis = Livro.verificar_disponibilidade(ano)
print(f'Livros Disponíveis do ano {ano}: {livros_disponiveis}')
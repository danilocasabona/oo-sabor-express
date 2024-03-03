# 1. Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.

class Livro:

    def __init__ (self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True

    # 2. Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e ano de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.
    def __str__(self):
        return f'Título: {self.titulo} | Autor: {self.autor} | Ano de publicação: {self.ano_publicacao}'
    
    # 3. Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.
    def emprestar(self):
        self.disponivel = False
        # print(f'O livro {self.titulo} está disponível.')
    
    # 4. Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.
    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = []
        for livro in Livro.livros:
            if livro.disponivel and livro.ano_publicacao == ano:
                livros_disponiveis.append(livro)
        return livros_disponiveis
        
livro1 = Livro('O Senhor dos Anéis', 'J.R.R. Tolkien', 1954)
livro2 = Livro('O Hobbit', 'J.R.R. Tolkien', 1937)
livro3 = Livro('As Duas Torres', 'J.R.R. Tolkien', 1954)

Livro.livros = [livro1, livro2, livro3]

# 5. Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.

    # No arquivo biblioteca.py insira from desafio6 import Livro

# 6. No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.
        
        # Insira no arquivo biblioteca.py
        #livro4 = Livro('O Senhor dos Anéis', 'J.R.R. Tolkien', 1954)
        # livro4.emprestar()
        # print(livro4.disponivel)

# 7. No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.

# Código do arquivo biblioteca.py
# ano = 1954
# livros_disponiveis = Livro.verificar_disponibilidade(ano)
# print(f'Livros Disponíveis do ano {ano}: {livros_disponiveis}')

# 8. Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py, instancie dois objetos da classe Livro e exiba a mensagem formatada utilizando o método str.

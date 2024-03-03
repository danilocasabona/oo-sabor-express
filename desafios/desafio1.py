# Crie uma classe chamada Musica com os seguintes atributos e crie 3 objetos definindo cada atributo.

class Musica:
    nome = ''
    artista = ''
    duracao = int

class Restaurante:
    nome = ''
    categoria = ''
    ativo = False


# Crie 3 objetos definindo cada atributo.
    
musica1 = Musica()
musica1.nome = 'Bohemian Rhapsody'
musica1.artista = 'Queen'
musica1.duracao = 355

musica2 = Musica()
musica2.nome = 'Imagine'
musica2.artista = 'John Lennon'
musica2.duracao = 183

musica3 = Musica()
musica3.nome = 'Shape of You'
musica3.artista = 'Ed Sheeran'
musica3.duracao = 234

Musica4 = Musica()
Musica4.nome = 'Amor Perfeito'
Musica4.artista = 'Bell Marques'
Musica4.duracao = 300

# 1. Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praca'
restaurante_praca.categoria = 'Italiana'


# 2. Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.

print(restaurante_praca.nome)

# 3. Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.

print(restaurante_praca.ativo)

# 4. Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria.

categoria = restaurante_praca.categoria
print(categoria)

# 5. Altere o valor do atributo nome para 'Bistrô'.

restaurante_praca.nome = 'Bistro'
print(restaurante_praca.nome)

# 6. Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.
restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'
print(restaurante_pizza.nome, restaurante_pizza.categoria)

# 7. Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.
print(restaurante_pizza.categoria)

# 8. Adicione uma lista de restaurantes à variável restaurantes.
restaurante1 = Restaurante()
restaurante1.nome = 'Bistro'
restaurante1.categoria = 'Italiana'
restaurante2 = Restaurante()
restaurante2.nome = 'Pizza Place'
restaurante2.categoria = 'Fast Food'
restaurante3 = Restaurante()
restaurante3.nome = 'O tal'
restaurante3.categoria = 'Boteco'
restaurantes = [restaurante1, restaurante2, restaurante3]
print(dir(restaurantes))

# 9. Mude o estado da instância restaurante_pizza para ativo.
restaurante_pizza.ativo = True

# 10. Verifique se restaurante_pizza está ativo.
print(restaurante_pizza.ativo)

# 11. Imprima no console o nome e a categoria da instância restaurante_praca.
print(restaurante_praca.nome, restaurante_praca.categoria)
# 1. Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.

class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

carro1 = Carro('Fusca', 'Vermelho', 1969)
carro2 = Carro('Gol', 'Preto', 1970)
carro3 = Carro('Palio', 'Branco', 1971)

print(carro1.modelo)
print(carro2.cor)
print(carro3.ano)

# 2. Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.

class Restaurante:
    def __init__(self, nome, categoria, ativo, custo, avaliacao):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.custo = custo
        self.avaliacao = avaliacao

restaurante1 = Restaurante('Praça', 'Boteco', True, 'R$ 50', '5 estrelas')

# 3. Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.

class Restaurantes:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        ativo = False

# 4. Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.
    def __str__(self):
        return f'{self.nome} - {self.categoria}'
    
restaurante2 = Restaurantes('Sushi', 'Japones')
print(restaurante2)

# 5. Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.

class Cliente:
    def __init__(self, nome, idade, sexo, cpf):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.cpf = cpf

cliente1 = Cliente('João', 30, 'Masculino', '123456789')
cliente2 = Cliente('Maria', 25, 'Feminino', '987654321')
cliente3 = Cliente('Pedro', 40, 'Masculino', '555555555')
print(cliente1.nome)
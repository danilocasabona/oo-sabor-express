# Crie uma nova classe chamada Pessoa com atributos como nome, idade e profissão. Adicione um método especial __str__ para imprimir uma representação em string da pessoa. Implemente também um método de instância chamado aniversario que aumenta a idade da pessoa em um ano. Por fim, adicione uma propriedade chamada saudacao que retorna uma mensagem de saudação personalizada com base na profissão da pessoa.

class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
    
    def __str__(self):
        return f'{self.nome}, {self.idade}, {self.profissao}'
    
    def aniversario(self):
        self.idade += 1

    @property
    def saudacao(self):
        if self.profissao == 'professor':
            return f'Olá, meu nome é {self.nome} e sou professor.'
        elif self.profissao == 'estudante':
            return f'Olá, meu nome é {self.nome} e sou estudante.'
        else:
            return f'Olá, meu nome é {self.nome} e sou desenvolvedor.'
        

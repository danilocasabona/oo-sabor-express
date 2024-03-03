# 1. Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self._ativo = False

# 2. Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.
    
    def __str__(self):
            return f'Titular: {self.titular}\nSaldo: R${self.saldo}'

conta1 = ContaBancaria('João', 1000)
conta2 = ContaBancaria('Maria', 2000)

print(conta1)
print(conta2)

# 3. Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.

@classmethod
def ativar_conta(cls, conta):
        cls._ativo = True
        print("Conta ativada")

conta3 = ContaBancaria('Pedro', 3000)
print(f'Antes de ativar: Conta Ativa? {conta3._ativo}')
ContaBancaria.ativar_conta(conta3)
print(f'Depois de ativar: Conta Ativa? {conta3._ativo}')

# 4. Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.
    
class ContaBancariaPythonica:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return self._ativo


# 5. Crie uma instância da classe e imprima o valor da propriedade titular.

conta4 = ContaBancariaPythonica('Pedro', 3000)
print(f'O titular da conta 4 é: {conta4.titular}')

# 6. Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.

class ClienteBanco:
      def __init__(self, nome, idade, profissao, endereco, telefone):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
        self.endereco = endereco
        self.telefone = telefone

titular4 = ClienteBanco('Paulo', 25, 'programador', 'Rua A', '123456789')
titular5 = ClienteBanco('Maria', 30, 'estudante', 'Rua B', '987654321')
titular6 = ClienteBanco('João', 35, 'professor', 'Rua C', '555555555')

# 6. Crie um método de classe para a conta ClienteBanco.

@classmethod
class ClienteBanco:
    # ... (outros métodos e atributos)

    @classmethod
    def criar_conta(cls, titular, saldo_inicial):
        conta = ContaBancariaPythonica(titular, saldo_inicial)
        return conta

# Exemplo de uso do método de classe
conta_cliente1 = ClienteBanco.criar_conta("Ana", 2000)
print(f"Conta de {conta_cliente1.titular} criada com saldo inicial de R${conta_cliente1.saldo}")

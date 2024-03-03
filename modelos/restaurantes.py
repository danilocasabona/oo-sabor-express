from modelos.avaliacao import Avaliacao

class Restaurante:
    """Representa um restaurante e suas características."""

    restaurantes = []

    def __init__(self, nome, categoria):
        """
        Inicializa uma instância de Restaurante.

        Parâmetros:
        - nome (str): O nome do restaurante.
        - categoria (str): A categoria do restaurante.
        """
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self.restaurantes.append(self)

    def __str__(self):
         """Retorna uma representação em string do restaurante."""
        return f'{self._nome} - {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        """Exibe uma lista formatada de todos os restaurantes."""
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliaçao'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacao).ljust(25)} | {restaurante.ativo}')
    
    @property
    def ativo(self):
        """Retorna um símbolo indicando o estado de atividade do restaurante."""
        return '☑' if self._ativo else '☐'
            
    def alternar_ativo(self):
        """Alterna o estado de atividade do restaurante."""
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        """
        Registra uma avaliação para o restaurante.

        Parâmetros:
        - cliente (str): O nome do cliente que fez a avaliação.
        - nota (float): A nota atribuída ao restaurante (entre 1 e 5).
        """
        if 0 < nota <= 5:
            self._avaliacao.append(Avaliacao(cliente, nota))
    
    @property
    def media_avaliacao(self):
        """Calcula e retorna a média das avaliações do restaurante."""
        if len(self._avaliacao) > 0:
            return round(sum([avaliacao._nota for avaliacao in self._avaliacao]) / len(self._avaliacao), 1)
        else:
            return '-'
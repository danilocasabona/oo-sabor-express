
from modelos.restaurantes import Restaurante

restaurante_praca = Restaurante('praça', 'Boteco')
# restaurante_mexicano = Restaurante('mexicano', 'Mexicano')
# restaurante_japones = Restaurante('japones', 'Japonesa')
# restaurante_mexicano.alternar_ativo()
restaurante_praca.receber_avaliacao('Maria', 5)
restaurante_praca.receber_avaliacao('João', 4)
restaurante_praca.receber_avaliacao('Pedro', 8)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Gui', 5)
restaurante_praca.receber_avaliacao('Lais', 4)
restaurante_praca.receber_avaliacao('Emy', 1)

def main():
    """Retorna o Restaurante no arquivo main"""
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
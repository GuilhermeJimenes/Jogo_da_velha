class AleatorioJogadas:
    def __init__(self, entrada):
        self.IEntrada = entrada

    # Jogador que joga de forma aleatoria
    def aleatorioJoga(self):
        from random import randint
        jogadaAleatoria = randint(0, 8)
        while not self.IEntrada.valida(jogadaAleatoria):
            jogadaAleatoria = randint(0, 8)
        return jogadaAleatoria
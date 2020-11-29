class PreJogos:
    def __init__(self, getValoresTela):
        self.TipoJogadorUm = None
        self.TipoJogadorDois = None
        self.IValoresTela = getValoresTela

    def getTipoJogadorUm(self):
        if self.IValoresTela:
            return self.IValoresTela['player1'][0]

    def getTipoJogadorDois(self):
        if self.IValoresTela:
            return self.IValoresTela['player2'][0]

    def getTiposJogadoresDaRodada(self):
        return self.getTipoJogadorUm(), self.getTipoJogadorDois()

    # retorna a quantidade de paridas escolhida
    def quantidadeDePartidasEscolhida(self):
        if self.IValoresTela:
            if int(self.IValoresTela['partidas']) < 1:
                return 1
            else:
                return int(self.IValoresTela['partidas'])

class PreJogosCtrl:
    def __init__(self, sensores, preJogo, dadosFixos):
        self.ISensores = sensores
        self.IPreJogo = preJogo
        self.IDadosFixos = dadosFixos

    def getTiposJogadoresCtrl(self):
        return self.IPreJogo.getTipoJogadorUm(), self.IPreJogo.getTipoJogadorDois()

    def getTipoJogadorPelaVezCtrl(self):
        if self.ISensores.vezDoJogadorUm():
            return self.IPreJogo.getTipoJogadorUm()
        else:
            return self.IPreJogo.getTipoJogadorDois()

    # def getTipoJogadorPelaPeca(self, peca):
    #     if self.IDadosFixos.getJogadorUmPeca() == peca:
    #         return self.IPreJogo.getTipoJogadorUm()
    #     else:
    #         return self.IPreJogo.getTipoJogadorDois()

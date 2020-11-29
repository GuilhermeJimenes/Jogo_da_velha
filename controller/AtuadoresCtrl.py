class AtuadoresCtrl:
    def __init__(self, atuadores, preJogoCtrl):
        self.IAtuadores = atuadores
        self.IPreJogoCtrl = preJogoCtrl

    def jogadaJogadoresCtrl(self):
        tipoJogadores = self.IPreJogoCtrl.getTipoJogadorPelaVezCtrl()
        return self.IAtuadores.jogadaJogadores(tipoJogadores)

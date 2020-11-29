class TabuleiroCtrl:
    def __init__(self, ambiente, entradas, preJogo, inteligencia,
                 telaTabuleiro, preJogoCtrl, fimDeJogosCtrl,
                 pecasCtrl, atuadoresCtrl, todosTiposJogadores):
        self.IAmbiente = ambiente
        self.IEntradas = entradas
        self.IPreJogo = preJogo
        self.IInteligencia = inteligencia
        self.ITelaTabuleiro = telaTabuleiro
        self.IPreJogoCtrl = preJogoCtrl
        self.IFimDeJogosCtrl = fimDeJogosCtrl
        self.IPecasCtrl = pecasCtrl
        self.IAtuadoresCtrl = atuadoresCtrl
        self.ITodosTiposJogadores = todosTiposJogadores

    def fluxoDeJogo(self):
        tipos = self.ITodosTiposJogadores

        self.ITelaTabuleiro.tabuleiro()
        while True:
            self.extrairDadosCtrl()
            if self.efeitosDasAcoes():
                if self.IPreJogoCtrl.getTipoJogadorPelaVezCtrl() != tipos[0]:
                    self.extrairDadosCtrl()
                break
        self.ITelaTabuleiro.limpaTabuleiro()

    def extrairDadosCtrl(self):
        tipos = self.ITodosTiposJogadores

        if self.IPreJogoCtrl.getTipoJogadorPelaVezCtrl() == tipos[0]:
            self.ITelaTabuleiro.extrairDados(False)
        else:
            self.ITelaTabuleiro.extrairDados(100)

    def efeitosDasAcoes(self):
        jogada, peca = self.jogadaQualquerJogador()

        self.IInteligencia.guardaEstado()
        self.IAmbiente.setCampo(jogada, peca)
        self.IEntradas.setTodosJogadasDaRodada(jogada)
        self.IInteligencia.guardaEstado()
        if self.IFimDeJogosCtrl.fimDeJogoCtrl(peca):
            return True

    def jogadaQualquerJogador(self):
        tipos = self.ITodosTiposJogadores

        peca = self.IPecasCtrl.getPecasPelaVezCtrl()
        jogada = self.IAtuadoresCtrl.jogadaJogadoresCtrl()
        if jogada == tipos[0]:
            jogada = self.ITelaTabuleiro.insercaoClique()
            while not self.IEntradas.valida(jogada):
                jogada = self.ITelaTabuleiro.jogadaInvalida()
            self.ITelaTabuleiro.preencherClique(peca)
        else:
            self.ITelaTabuleiro.insercaoManual(jogada, peca)
        return jogada, peca

class FimDeJogosCtrl:
    def __init__(self, preJogoCtrl, telaTabuleiro, fimDeJogo,
                 baseDeDadosCtrl, getTodosTiposJogadores,
                 performances, inteligencia, entradas):
        self.IPreJogoCtrl = preJogoCtrl
        self.ITelaTabuleiro = telaTabuleiro
        self.IFimDeJogo = fimDeJogo
        self.IBaseDeDadosCtrl = baseDeDadosCtrl
        self.IGetTodosTiposJogadores = getTodosTiposJogadores
        self.IPerformances = performances
        self.IInteligencia = inteligencia
        self.IEntradas = entradas

    def fimDeJogoCtrl(self, peca):
        jogadores = self.IPreJogoCtrl.getTiposJogadoresCtrl()
        tipos = self.IGetTodosTiposJogadores

        if self.naoVelhaCtrl(peca):
            if tipos[0] in jogadores:
                self.ITelaTabuleiro.popupGanhou(peca)
            return True
        if self.velhaCtrl():
            if tipos[0] in jogadores:
                self.ITelaTabuleiro.popupVelha()
            return True

    # controla o fluxo de fim de jogo
    def naoVelhaCtrl(self, peca):
        if self.IFimDeJogo.ganhou(peca):
            self.IPerformances.ConstroiPerformance(peca)
            self.aplicaReforco(peca)
            self.IBaseDeDadosCtrl.salvaAquivoCtrl()
            return True

    # retorna verificação de velha
    def velhaCtrl(self):
        if self.IFimDeJogo.velha():
            self.IPerformances.ConstroiPerformance()
            self.IBaseDeDadosCtrl.salvaAquivoCtrl()
            return True
        return False

    def aplicaReforco(self, peca):
        arvore = self.IInteligencia.getArvore()
        self.IInteligencia.reforco(arvore, peca)

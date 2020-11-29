class DificilSensores:
    def __init__(self, sensores, aleatorioJogadas, getTodasPecas):
        self.ISensores = sensores
        self.IAleatorioJogadas = aleatorioJogadas
        self.IGetTodasPecas = getTodasPecas

    # isso garante que o agente dificil possa jogar com outro dificil
    def auxPecas(self):
        if self.ISensores.vezDoJogadorUm():
            return self.IGetTodasPecas[0], self.IGetTodasPecas[1]
        else:
            return self.IGetTodasPecas[1], self.IGetTodasPecas[0]

    def auxVerificaVitoria(self):
        pecaPcDificil, pecaOutroJogador = self.auxPecas()
        seDificilGanha = self.ISensores.verificaSeGanha(pecaPcDificil)
        seDificilPerde = self.ISensores.verificaSeGanha(pecaOutroJogador)
        if seDificilGanha != -1:
            return seDificilGanha
        elif seDificilPerde != -1:
            return seDificilPerde
        else:
            return self.IAleatorioJogadas.aleatorioJoga()

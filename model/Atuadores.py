class Atuadores:
    def __init__(self, AleatorioJogadas, dificilJogadas, getTodosTiposJogadores, inteligente):
        self.IAleatorioJogadas = AleatorioJogadas
        self.IDificilJogadas = dificilJogadas
        self.IGetTodosTiposJogadores = getTodosTiposJogadores
        self.IInteligente = inteligente

    # define o tipo de jogada para o jogador escolhido
    def jogadaJogadores(self, tipoJogadores):
        tipos = self.IGetTodosTiposJogadores

        jogada = tipos[0]
        if tipoJogadores == tipos[1]:
            jogada = self.IAleatorioJogadas.aleatorioJoga()
        elif tipoJogadores == tipos[2]:
            jogada = self.IDificilJogadas.dificilJoga()
        elif tipoJogadores == tipos[3]:
            jogada = self.IInteligente.inteligenteJoga()
        return jogada

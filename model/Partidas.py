class Partidas:
    def __init__(self):
        self.IPartidaAtual = 1

    def getPartidaAtual(self):
        return self.IPartidaAtual

    def fimDaPartida(self):
        self.IPartidaAtual += 1

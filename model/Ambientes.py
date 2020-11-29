class Ambientes:
    def __init__(self):
        self.Campo = ['_'] * 9

    # retorna o campo
    def getCampo(self):
        return self.Campo

    def setCampo(self, jogada, peca):
        self.Campo[jogada] = peca
        return self.Campo

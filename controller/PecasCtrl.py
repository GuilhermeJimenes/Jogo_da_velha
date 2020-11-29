class PecasCtrl:
    def __init__(self, sensores, peca):
        self.ISensores = sensores
        self.IPeca = peca

    def getPecasPelaVezCtrl(self):
        if self.ISensores.vezDoJogadorUm():
            return self.IPeca.getJogadorUmPeca()
        else:
            return self.IPeca.getJogadorDoisPeca()

from app.Dependencia import Dependencia


class Main(Dependencia):
    def __init__(self):
        super().__init__()
        self.fluxoPrincipal()

    def fluxoPrincipal(self):
        partidas = self.preJogos().quantidadeDePartidasEscolhida()
        while partidas != 0:
            tabuleiroCtrl = self.tabuleirosCtrl()
            tabuleiroCtrl.fluxoDeJogo()
            partidas = partidas - 1
            self.apagaObjetos()


if __name__ == '__main__':
    Main()

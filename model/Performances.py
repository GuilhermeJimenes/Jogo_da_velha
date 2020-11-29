class Performances:
    def __init__(self, preJogos, nomeArquivoPerformance, arquivosExternos, getTodasPecas):
        self.IPreJogos = preJogos
        self.INomeArquivoPerformance = nomeArquivoPerformance
        self.IArquivosExternos = arquivosExternos
        self.IGetTodasPecas = getTodasPecas
        self.Performance = {}
        self.partidaAtual = 1

    @staticmethod
    def esqueletoPerformance():
        return {
            "jogadorUm": {"tipo": "", "vitoria": [0], "peca": ""},
            "jogadorDois": {"tipo": "", "vitoria": [0], "peca": ""},
            "comum": {"partida": 1, "empates": [0]}
        }

    def __setPerformance(self):
        if not self.Performance or self.Performance == {}:
            nomeArquivo = self.INomeArquivoPerformance
            Performance = self.IArquivosExternos.pega(nomeArquivo)
            if not Performance or Performance == {}:
                Performance = self.esqueletoPerformance()
            self.Performance = Performance

    def getPerformance(self):
        if not self.Performance or self.Performance == {}:
            self.__setPerformance()
        return self.Performance

    def setTipos(self):
        tipoJogadorUm, tipoJogadorDois = self.IPreJogos.getTiposJogadoresDaRodada()
        self.getPerformance()['jogadorUm']['tipo'] = tipoJogadorUm
        self.getPerformance()['jogadorDois']['tipo'] = tipoJogadorDois

    def setResultado(self, vitoriaUm=0, vitoriaDois=0, empate=0):
        ultimaVitoriaUm = self.getPerformance()['jogadorUm']['vitoria'][-1]
        ultimaVitoriaDois = self.getPerformance()['jogadorDois']['vitoria'][-1]
        ultimoEmpate = self.getPerformance()['comum']['empates'][-1]

        self.getPerformance()['jogadorUm']['vitoria'].append(ultimaVitoriaUm + vitoriaUm)
        self.getPerformance()['jogadorDois']['vitoria'].append(ultimaVitoriaDois + vitoriaDois)
        self.getPerformance()['comum']['empates'].append(ultimoEmpate + empate)

    def setPecas(self):
        pecasUm, pecasDois = self.IGetTodasPecas
        self.getPerformance()['jogadorUm']['peca'] = pecasUm
        self.getPerformance()['jogadorDois']['peca'] = pecasDois

    def setPartida(self):
        self.limpaBase()
        self.partidaAtual += 1
        self.getPerformance()['comum']['partida'] = self.partidaAtual

    def limpaBase(self):
        if self.partidaAtual == 1:
            self.salvaBase(base={})
            self.Performance = {}
            self.__setPerformance()

    def salvaBase(self, base=None):
        if base is None:
            base = self.getPerformance()
        nomeArquivo = self.INomeArquivoPerformance
        self.IArquivosExternos.salva(base, nomeArquivo)

    def pontuacaoResultado(self, peca=None):
        pecasUm, pecasDois = self.IGetTodasPecas

        if peca == pecasUm:
            self.setResultado(vitoriaUm=1)
        elif peca == pecasDois:
            self.setResultado(vitoriaDois=1)
        elif peca is None:
            self.setResultado(empate=1)

    def ConstroiPerformance(self, peca=None):
        self.setPartida()
        self.setTipos()
        self.setPecas()
        self.pontuacaoResultado(peca)
        self.salvaBase()

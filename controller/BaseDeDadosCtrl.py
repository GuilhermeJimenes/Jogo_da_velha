class BaseDeDadosCtrl:
    def __init__(self, ambientes, baseDeDados, nomeArquivoIA, inteligencia):
        self.IAmbientes = ambientes
        self.IBaseDeDados = baseDeDados
        self.INomeArquivoIA = nomeArquivoIA
        self.IInteligencia = inteligencia

    def salvaAquivoCtrl(self):
        nomeArquivo = self.INomeArquivoIA
        self.IInteligencia.salvaJogadasNohZero()
        arvore = self.IInteligencia.getArvore()
        self.IBaseDeDados.salva(arvore, nomeArquivo)

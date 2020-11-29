class DadosFixos:
    def __init__(self):
        pass

    # retorna o Simbolo do jogador um
    def getJogadorUmPeca(self):
        return 'X'

    # retorna o Simbolo do jogador dois
    def getJogadorDoisPeca(self):
        return 'O'

    def getTodosTiposJogadores(self):
        return 'Humano', 'Facil', 'Dificil', 'Inteligente'

    def simboloCampoVazio(self):
        return '_'

    def nomeArquivoIA(self):
        return 'InteligenteDados'

    def nomeArquivoPerformance(self):
        return 'PerformanceDados'

    def getTodasPecas(self):
        return self.getJogadorUmPeca(), self.getJogadorDoisPeca()

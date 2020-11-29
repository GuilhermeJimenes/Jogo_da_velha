class Sensores:
    def __init__(self, ambiente, simboloCampoVazio, getTodasPecas):
        self.IAmbiente = ambiente
        self.ISimboloCampoVazio = simboloCampoVazio
        self.IJogadorUmPeca, self.IJogadorDoisPeca = getTodasPecas

    # retorna a posição do vetor que se jogada, ganha o jogo
    def verificaSeGanha(self, pecaQualquerJogador):
        simbolo = self.ISimboloCampoVazio
        campo = self.IAmbiente.getCampo()
        peca = pecaQualquerJogador

        if campo[0] == peca and campo[1] == peca:
            if campo[2] == simbolo:
                return 2
        if campo[0] == peca and campo[2] == peca:
            if campo[1] == simbolo:
                return 1
        if campo[1] == peca and campo[2] == peca:
            if campo[0] == simbolo:
                return 0

        if campo[3] == peca and campo[4] == peca:
            if campo[5] == simbolo:
                return 5
        if campo[3] == peca and campo[5] == peca:
            if campo[4] == simbolo:
                return 4
        if campo[4] == peca and campo[5] == peca:
            if campo[3] == simbolo:
                return 3

        if campo[6] == peca and campo[7] == peca:
            if campo[8] == simbolo:
                return 8
        if campo[6] == peca and campo[8] == peca:
            if campo[7] == simbolo:
                return 7
        if campo[7] == peca and campo[8] == peca:
            if campo[6] == simbolo:
                return 6

        if campo[0] == peca and campo[3] == peca:
            if campo[6] == simbolo:
                return 6
        if campo[0] == peca and campo[6] == peca:
            if campo[3] == simbolo:
                return 3
        if campo[3] == peca and campo[6] == peca:
            if campo[0] == simbolo:
                return 0

        if campo[1] == peca and campo[4] == peca:
            if campo[7] == simbolo:
                return 7
        if campo[1] == peca and campo[7] == peca:
            if campo[4] == simbolo:
                return 4
        if campo[4] == peca and campo[7] == peca:
            if campo[1] == simbolo:
                return 1

        if campo[2] == peca and campo[5] == peca:
            if campo[8] == simbolo:
                return 8
        if campo[2] == peca and campo[8] == peca:
            if campo[5] == simbolo:
                return 5
        if campo[5] == peca and campo[8] == peca:
            if campo[2] == simbolo:
                return 2

        if campo[0] == peca and campo[4] == peca:
            if campo[8] == simbolo:
                return 8
        if campo[0] == peca and campo[8] == peca:
            if campo[4] == simbolo:
                return 4
        if campo[4] == peca and campo[8] == peca:
            if campo[0] == simbolo:
                return 0

        if campo[2] == peca and campo[4] == peca:
            if campo[6] == simbolo:
                return 6
        if campo[2] == peca and campo[6] == peca:
            if campo[4] == simbolo:
                return 4
        if campo[4] == peca and campo[6] == peca:
            if campo[2] == simbolo:
                return 2
        return -1

    # verifica se o a quantida de X e O no campo são
    # iguais para determinar de quem é a vez de jogar
    def vezDoJogadorUm(self):
        campo = self.IAmbiente.getCampo()
        pecaUm = self.IJogadorUmPeca
        pecaDois = self.IJogadorDoisPeca

        if campo.count(pecaUm) == campo.count(pecaDois):
            return True
        elif campo.count(pecaUm) != campo.count(pecaDois):
            return False

    def rodadaAtual(self):
        campo = self.IAmbiente.getCampo()
        radadaAtual = 9 - campo.count('_')
        return radadaAtual

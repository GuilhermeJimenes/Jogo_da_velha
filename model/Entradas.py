class Entradas:
    def __init__(self, ambiente, simboloCampoVazio):
        self.IAmbiente = ambiente
        self.ISimboloCampoVazio = simboloCampoVazio
        self.EntradasEmOrdem = []

    # verifica se a jogada realizada é valida
    def valida(self, jogada):
        simbolo = self.ISimboloCampoVazio
        campo = self.IAmbiente.getCampo()

        if type(jogada) == int:
            if jogada in range(0, 9):
                if campo[jogada] == simbolo:
                    return True
        return False

    # define a primeira jogada, esse metodo tem o intuito de ajuda os
    # agentes a descobrir qual a primeira jogada realizada pelo jogador
    def setTodosJogadasDaRodada(self, entrada):
        self.EntradasEmOrdem.append(entrada)

    def getTodasJogadasDaRodada(self):
        return self.EntradasEmOrdem

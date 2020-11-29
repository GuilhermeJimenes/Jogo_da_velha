class FimDeJogos:
    def __init__(self, ambiente, simboloCampoVazio):
        self.IAmbiente = ambiente
        self.ISimboloCampoVazio = simboloCampoVazio

    # verifica se o campo ainda tem posições vazias
    def velha(self):
        simbolo = self.ISimboloCampoVazio
        if simbolo not in self.IAmbiente.getCampo():
            return True

    # verifica se algum dos jogadores formou uma
    # linha na horizontal, vertical ou diagonal
    def ganhou(self, peca):
        campo = self.IAmbiente.getCampo()

        if campo[0] == peca and campo[1] == peca and campo[2] == peca:
            return 1

        if campo[3] == peca and campo[4] == peca and campo[5] == peca:
            return 1

        if campo[6] == peca and campo[7] == peca and campo[8] == peca:
            return 1

        if campo[0] == peca and campo[3] == peca and campo[6] == peca:
            return 1

        if campo[1] == peca and campo[4] == peca and campo[7] == peca:
            return 1

        if campo[2] == peca and campo[5] == peca and campo[8] == peca:
            return 1

        if campo[0] == peca and campo[4] == peca and campo[8] == peca:
            return 1

        if campo[2] == peca and campo[4] == peca and campo[6] == peca:
            return 1

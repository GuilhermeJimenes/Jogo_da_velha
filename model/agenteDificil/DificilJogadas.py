class DificilJogadas:
    def __init__(self, ambiente, entrada, dificilSensores,
                 getJogadorUmPeca, simboloCampoVazio):
        self.IAmbiente = ambiente
        self.IEntrada = entrada
        self.IDificilSensores = dificilSensores
        self.IGetJogadorUmPeca = getJogadorUmPeca
        self.ISimboloCampoVazio = simboloCampoVazio
        self.Fodase = False

    # Jogador que nunca perde, sua base de dados esta toda no codigo
    def dificilJoga(self):
        pecaPcDificil, pecaOutroJogador = self.IDificilSensores.auxPecas()

        campo = self.IAmbiente.getCampo()

        if pecaPcDificil == self.IGetJogadorUmPeca:
            return self.dificilPrimeiro(campo, pecaPcDificil, pecaOutroJogador)
        else:
            return self.dificilSegundo()

    def dificilSegundo(self):
        todasJogadas = self.IEntrada.getTodasJogadasDaRodada()
        tamanho = len(todasJogadas)
        verifica = self.IDificilSensores.auxVerificaVitoria()

        if self.Fodase:
            return verifica
        if tamanho == 1:
            return self.primeiraRodada(todasJogadas)
        if tamanho == 3:
            return self.segundaRodada(todasJogadas, verifica)
        if tamanho == 5:
            return self.terceiraRodada(todasJogadas, verifica)
        print("Erro no jogador dificil quando é o segundo")

    def primeiraRodada(self, todasJogadas):
        if todasJogadas == [4]:
            return 6
        else:
            return 4

    def segundaRodada(self, todasJogadas, verifica):
        if todasJogadas[0] == 0:
            self.Fodase = True
            if todasJogadas == [0, 4, 1]:
                return verifica
            elif todasJogadas == [0, 4, 2]:
                return verifica
            elif todasJogadas == [0, 4, 3]:
                return verifica
            elif todasJogadas == [0, 4, 5]:
                return 8
            elif todasJogadas == [0, 4, 6]:
                return verifica
            elif todasJogadas == [0, 4, 7]:
                return 8
            elif todasJogadas == [0, 4, 8]:
                return 1

        elif todasJogadas[0] == 1:
            self.Fodase = True
            if todasJogadas == [1, 4, 0]:
                return verifica
            elif todasJogadas == [1, 4, 2]:
                return verifica
            elif todasJogadas == [1, 4, 3]:
                return 2
            elif todasJogadas == [1, 4, 5]:
                return 0
            elif todasJogadas == [1, 4, 6]:
                return 0
            elif todasJogadas == [1, 4, 7]:
                return 6
            elif todasJogadas == [1, 4, 8]:
                return 2

        elif todasJogadas[0] == 2:
            self.Fodase = True
            if todasJogadas == [2, 4, 0]:
                return verifica
            elif todasJogadas == [2, 4, 1]:
                return verifica
            elif todasJogadas == [2, 4, 3]:
                return 6
            elif todasJogadas == [2, 4, 5]:
                return verifica
            elif todasJogadas == [2, 4, 6]:
                return 1
            elif todasJogadas == [2, 4, 7]:
                return 6
            elif todasJogadas == [2, 4, 8]:
                return verifica

        elif todasJogadas[0] == 3:
            self.Fodase = True
            if todasJogadas == [3, 4, 0]:
                return verifica
            elif todasJogadas == [3, 4, 1]:
                return 2
            elif todasJogadas == [3, 4, 2]:
                return 0
            elif todasJogadas == [3, 4, 5]:
                return 2
            elif todasJogadas == [3, 4, 6]:
                return verifica
            elif todasJogadas == [3, 4, 7]:
                return 8
            elif todasJogadas == [3, 4, 8]:
                return 6

        elif todasJogadas[0] == 4:
            self.Fodase = True
            if todasJogadas == [4, 6, 0]:
                return verifica
            elif todasJogadas == [4, 6, 1]:
                return verifica
            elif todasJogadas == [4, 6, 2]:
                return 0
            elif todasJogadas == [4, 6, 3]:
                self.Fodase = False
                return 5
            elif todasJogadas == [4, 6, 5]:
                return verifica
            elif todasJogadas == [4, 6, 7]:
                self.Fodase = False
                return 1
            elif todasJogadas == [4, 6, 8]:
                return verifica

        elif todasJogadas[0] == 5:
            self.Fodase = True
            if todasJogadas == [5, 4, 0]:
                return 2
            elif todasJogadas == [5, 4, 1]:
                return 0
            elif todasJogadas == [5, 4, 2]:
                return verifica
            elif todasJogadas == [5, 4, 3]:
                return 2
            elif todasJogadas == [5, 4, 6]:
                return 8
            elif todasJogadas == [5, 4, 7]:
                return 6
            elif todasJogadas == [5, 4, 8]:
                return verifica

        elif todasJogadas[0] == 6:
            self.Fodase = True
            if todasJogadas == [6, 4, 0]:
                return verifica
            elif todasJogadas == [6, 4, 1]:
                return 2
            elif todasJogadas == [6, 4, 2]:
                return 1
            elif todasJogadas == [6, 4, 3]:
                return verifica
            elif todasJogadas == [6, 4, 5]:
                return 2
            elif todasJogadas == [6, 4, 7]:
                return verifica
            elif todasJogadas == [6, 4, 8]:
                return verifica

        elif todasJogadas[0] == 7:
            self.Fodase = True
            if todasJogadas == [7, 4, 0]:
                return 6
            elif todasJogadas == [7, 4, 1]:
                return 6
            elif todasJogadas == [7, 4, 2]:
                return 8
            elif todasJogadas == [7, 4, 3]:
                return 8
            elif todasJogadas == [7, 4, 5]:
                return 6
            elif todasJogadas == [7, 4, 6]:
                return verifica
            elif todasJogadas == [7, 4, 8]:
                return verifica

        elif todasJogadas[0] == 8:
            self.Fodase = True
            if todasJogadas == [8, 4, 0]:
                return 1
            elif todasJogadas == [8, 4, 1]:
                return 0
            elif todasJogadas == [8, 4, 2]:
                return verifica
            elif todasJogadas == [8, 4, 3]:
                return 0
            elif todasJogadas == [8, 4, 5]:
                return verifica
            elif todasJogadas == [8, 4, 6]:
                return verifica
            elif todasJogadas == [8, 4, 7]:
                return verifica

    def terceiraRodada(self, todasJogadas, verifica):
        self.Fodase = True
        if todasJogadas[:-1] == [4, 6, 3, 5]:
            if todasJogadas[-1] == 2:
                return 0
            else:
                return verifica
        elif todasJogadas[:-1] == [4, 6, 7, 1]:
            if todasJogadas[-1] == 2:
                return 8
            else:
                return verifica

    def dificilPrimeiro(self, campo, pecaPcInteligente, pecaOutroJogador):
        simboloVazio = self.ISimboloCampoVazio
        verifica = self.IDificilSensores.auxVerificaVitoria()
        # PC é o primeiro a jogar
        if campo[6] == simboloVazio:
            # Jogada 1
            return 6
        else:
            primeiraJogadorDois = self.IEntrada.getTodasJogadasDaRodada()[1]
            if primeiraJogadorDois == 0:
                if campo[7] == pecaPcInteligente:
                    if campo[8] == pecaOutroJogador:
                        if campo[4] == pecaPcInteligente:
                            # Jogada 4
                            return verifica
                        else:
                            # Jogada 3.2
                            return 4
                    else:
                        # Jogada 3.1
                        return 8
                else:
                    # Jogada 2
                    return 7
            elif primeiraJogadorDois == 1:
                if campo[8] == pecaPcInteligente:
                    if campo[7] == pecaOutroJogador:
                        if campo[4] == pecaPcInteligente:
                            # Jogada 4
                            return verifica
                        else:
                            # Jogada 3.2
                            return 4
                    else:
                        # Jogada 3.1
                        return 7
                else:
                    # Jogada 2
                    return 8
            elif primeiraJogadorDois == 2:
                if campo[0] == pecaPcInteligente:
                    if campo[3] == pecaOutroJogador:
                        if campo[8] == pecaPcInteligente:
                            # Jogada 4
                            return verifica
                        else:
                            # Jogada 3.2
                            return 8
                    else:
                        # Jogada 3.1
                        return 3
                else:
                    # Jogada 2
                    return 0

            elif primeiraJogadorDois == 3:
                if campo[7] == pecaPcInteligente:
                    if campo[8] == pecaOutroJogador:
                        if campo[4] == pecaPcInteligente:
                            # Jogada 4
                            return verifica
                        else:
                            # Jogada 3.2
                            return 4
                    else:
                        # Jogada 3.1
                        return 8
                else:
                    # Jogada 2
                    return 7

            elif primeiraJogadorDois == 4:
                if campo[2] == simboloVazio:
                    return 2
                else:
                    return verifica

            elif primeiraJogadorDois == 5:
                if campo[0] == pecaPcInteligente:
                    if campo[3] == pecaOutroJogador:
                        if campo[4] == pecaPcInteligente:
                            # Jogada 4
                            return verifica
                        else:
                            # Jogada 3.2
                            return 4
                    else:
                        # Jogada 3.1
                        return 3
                else:
                    # Jogada 2
                    return 0

            elif primeiraJogadorDois == 7:
                if campo[3] == pecaPcInteligente:
                    if campo[0] == pecaOutroJogador:
                        if campo[4] == pecaPcInteligente:
                            # Jogada 4
                            return verifica
                        else:
                            # Jogada 3.2
                            return 4
                    else:
                        # Jogada 3.1
                        return 0
                else:
                    # Jogada 2
                    return 3

            elif primeiraJogadorDois == 8:
                if campo[3] == pecaPcInteligente:
                    if campo[0] == pecaOutroJogador:
                        if campo[4] == pecaPcInteligente:
                            # Jogada 4
                            return verifica
                        else:
                            # Jogada 3.2
                            return 4
                    else:
                        # Jogada 3.1
                        return 0
                else:
                    # Jogada 2
                    return 3

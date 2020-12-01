class Inteligencia:
    def __init__(self, nomeArquivoIA, arquivosExternos, ambientes,
                 entradas, todosTiposJogadores, preJogos):
        self.INomeArquivoIA = nomeArquivoIA
        self.IArquivosExternos = arquivosExternos
        self.IAmbientes = ambientes
        self.IEntradas = entradas
        self.ITodosTiposJogadores = todosTiposJogadores
        self.IPreJogos = preJogos
        self.Arvore = {}

    def __esqueletoNoh(self):
        return self.__definindoFolha(
            {'arestas': [''] * 9, 'score': [0] * 9,
             'estado': self.IAmbientes.getCampo().copy()})

    def getArvore(self):
        if self.Arvore == {} or self.Arvore is None:
            self.__setArvore(self.__esqueletoNoh())
        return self.Arvore

    @staticmethod
    def __folha():
        return float('inf')

    def __setArvore(self, noh):
        nomeArquivo = self.INomeArquivoIA
        arvore = self.IArquivosExternos.pega(nomeArquivo)
        if not arvore or arvore == {}:
            arvore = noh
        self.Arvore = arvore

    def salvaJogadasNohZero(self):
        jogadasDaRodada = self.IEntradas.getTodasJogadasDaRodada()
        try:
            if jogadasDaRodada not in self.getArvore()['jogadas']:
                self.getArvore()['jogadas'].append(self.IEntradas.getTodasJogadasDaRodada())
        except:
            self.getArvore()['jogadas'] = []
            self.getArvore()['jogadas'].append(self.IEntradas.getTodasJogadasDaRodada())

    def guardaEstado(self):
        inteligente = self.ITodosTiposJogadores[3]
        if inteligente in self.IPreJogos.getTiposJogadoresDaRodada():
            self.__novoNoh(self.__esqueletoNoh())

    # adicionar infinito no scores que não podem mais ser jogados
    def __definindoFolha(self, noh):
        for posicao, peca in enumerate(noh['estado']):
            if peca != '_':
                noh['score'][posicao] = self.__folha()
        return noh

    def pegaQualquerNoh(self, j=None, umParaPegaScore=0):
        if j is None:
            j = self.IEntradas.getTodasJogadasDaRodada()
        qntJogadas = len(j)
        arvore = self.getArvore()

        if qntJogadas == (0 - umParaPegaScore):
            # print("pegaQualquerNoh 0")
            return

        elif qntJogadas == (1 - umParaPegaScore):
            return arvore

        elif qntJogadas == (2 - umParaPegaScore):
            return arvore['arestas'][j[0]]

        elif qntJogadas == (3 - umParaPegaScore):
            return arvore['arestas'][j[0]]['arestas'][j[1]]

        elif qntJogadas == (4 - umParaPegaScore):
            return arvore['arestas'][j[0]]['arestas'][j[1]]['arestas'][j[2]]

        elif qntJogadas == (5 - umParaPegaScore):
            return arvore['arestas'][j[0]]['arestas'][j[1]]['arestas'][j[2]]['arestas'][j[3]]

        elif qntJogadas == (6 - umParaPegaScore):
            return arvore['arestas'][j[0]]['arestas'][j[1]]['arestas'][j[2]]['arestas'][j[3]][
                'arestas'][j[4]]

        elif qntJogadas == (7 - umParaPegaScore):
            return arvore['arestas'][j[0]]['arestas'][j[1]]['arestas'][j[2]]['arestas'][j[3]][
                'arestas'][j[4]]['arestas'][j[5]]

        elif qntJogadas == (8 - umParaPegaScore):
            return arvore['arestas'][j[0]]['arestas'][j[1]]['arestas'][j[2]]['arestas'][j[3]][
                'arestas'][j[4]]['arestas'][j[5]]['arestas'][j[6]]

        elif qntJogadas == (9 - umParaPegaScore):
            return arvore['arestas'][j[0]]['arestas'][j[1]]['arestas'][j[2]]['arestas'][j[3]][
                'arestas'][j[4]]['arestas'][j[5]]['arestas'][j[6]]['arestas'][j[7]]

        elif qntJogadas == (10 - umParaPegaScore):
            return arvore['arestas'][j[0]]['arestas'][j[1]]['arestas'][j[2]]['arestas'][j[3]][
                'arestas'][j[4]]['arestas'][j[5]]['arestas'][j[6]]['arestas'][j[7]]['arestas'][j[8]]
        else:
            print(f'''
            ERRO AO PEGAR ULTIMO NÓ! METODO pegaUltimoNoh.
            Quantidade de jogadas do inteligente nessa rodada: {qntJogadas}.
            Todas as jogadas do inteligente nessa rodada: {j};
            Arvore atual: {arvore}.
            ''')
            exit()

    def __novoNoh(self, noh):
        j = self.IEntradas.getTodasJogadasDaRodada()
        qntJogadas = len(j)

        if qntJogadas == 0:
            if self.Arvore != {} and self.Arvore is not None:
                return
            else:
                self.__setArvore(self.__esqueletoNoh())
                return
        elif 0 < qntJogadas < 10:
            nohAntigo = self.pegaQualquerNoh()['arestas'][j[qntJogadas - 1]]
            if nohAntigo != '':
                return
            elif nohAntigo == '':
                # print(f'novoNoh {qntJogadas - 1}!')
                self.pegaQualquerNoh()['arestas'][j[qntJogadas - 1]] = noh
                return
        else:
            print(f'''
            ERRO AO CRIAR NOVO NÓ! METODO novoNoh.
            Quantidade de jogadas do inteligente nessa rodada: {qntJogadas}.
            Todas as jogadas do inteligente nessa rodada: {j};
            Nó que se está tentando inserir: {noh}.
            ''')
            exit()

    def quantidadeReforco(self, pecaQueGanhou):
        tipoJogadorUm, tipoJogadorDois = self.IPreJogos.getTiposJogadoresDaRodada()
        reforcoUm = 0
        reforcoDois = 0
        inteligente = self.ITodosTiposJogadores[3]

        if tipoJogadorDois == inteligente:
            if pecaQueGanhou == 'X':
                reforcoUm = 1
            else:
                reforcoUm = -1

        if tipoJogadorUm == inteligente:
            if pecaQueGanhou == 'O':
                reforcoDois = 1
            else:
                reforcoDois = -1

        return reforcoUm, reforcoDois

    def reforco(self, arvore, pecaQueGanhou):
        reforcoUm, reforcoDois = self.quantidadeReforco(pecaQueGanhou)
        j = self.IEntradas.getTodasJogadasDaRodada()
        qntJogadas = len(j)
        try:
            if qntJogadas >= 1:
                # print("reforco 1!")
                self.pegaQualquerNoh(j[:1])['score'][j[0]] += reforcoDois
            else:
                return

            if qntJogadas >= 2:
                # print("reforco 2!")
                self.pegaQualquerNoh(j[:2])['score'][j[1]] += reforcoUm
            else:
                return

            if qntJogadas >= 3:
                # print("reforco 3!")
                self.pegaQualquerNoh(j[:3])['score'][j[2]] += reforcoDois
            else:
                return

            if qntJogadas >= 4:
                # print("reforco 4!")
                self.pegaQualquerNoh(j[:4])['score'][j[3]] += reforcoUm
            else:
                return

            if qntJogadas >= 5:
                # print("reforco 5!")
                self.pegaQualquerNoh(j[:5])['score'][j[4]] += reforcoDois
            else:
                return

            if qntJogadas >= 6:
                # print("reforco 6!")
                self.pegaQualquerNoh(j[:6])['score'][j[5]] += reforcoUm
            else:
                return

            if qntJogadas >= 7:
                # print("reforco 7!")
                self.pegaQualquerNoh(j[:7])['score'][j[6]] += reforcoDois
            else:
                return

            if qntJogadas >= 8:
                # print("reforco 8!")
                self.pegaQualquerNoh(j[:8])['score'][j[7]] += reforcoUm
            else:
                return

            if qntJogadas >= 9:
                # print("reforco 9!")
                self.pegaQualquerNoh(j[:9])['score'][j[8]] += reforcoDois
            else:
                return
            return
        except:
            print(f'''
            ERRO ATRIBUIR REFORÇO! METODO reforco.
            Quantidade de jogadas do inteligente nessa rodada: {qntJogadas}.
            Todas as jogadas do inteligente nessa rodada: {j};
            Arvore atual: {arvore}.
            ''')
            exit()

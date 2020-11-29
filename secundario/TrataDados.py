from model.ArquivosExternos import ArquivosExternos
# import sys


class TrataDados:
    def __init__(self):
        self.TodosOsNohs = []
        self.NohsNaoVisitados = []
        # sys.setrecursionlimit(10000)  # usar em caso de erro de limite de recusão

    def percorreArvore(self, arvore):
        self.__salvaNohZero(arvore.copy())
        for largura in range(9):
            noh = arvore['arestas'][largura]
            if noh != '':
                self.__achouNoh(noh)
        self.__salvaNoh()
        return self.__ordenaNohs(self.TodosOsNohs)

    def __salvaNohZero(self, arvore):
        nohZero = arvore.copy()
        nohZero.pop('arestas')
        self.TodosOsNohs.append(nohZero)

    def __achouNoh(self, noh):
        self.NohsNaoVisitados.append(noh)
        nohSemAresta = noh.copy()
        nohSemAresta.pop('arestas')
        self.TodosOsNohs.append(nohSemAresta)

    def __salvaNoh(self):
        for noh in self.NohsNaoVisitados:
            self.NohsNaoVisitados.remove(noh)
            self.percorreArvore(noh)

    def __ordenaNohs(self, nohsEncontrados):
        return sorted(nohsEncontrados, key=lambda noh: noh['partida'])


if __name__ == '__main__':
    arvore = ArquivosExternos().pega('InteligenteDados')
    todosOsNohs = TrataDados().percorreArvore(arvore)
    print('arvore: ', arvore)
    print()
    print('todosOsNohs: ', todosOsNohs)

import pickle
import os


class ArquivosExternos:
    def __init__(self):
        self.diretorio = 'C:/jogo_da_velha_json/'

    # salva dados em um arquivo
    def salva(self, base, nomeArquivo):
        self.criaDiretorio()
        nomeArquivo = f'{nomeArquivo}.json'
        caminho = self.diretorio + nomeArquivo

        with open(caminho, 'w+b') as arquivo:
            pickle.dump(base, arquivo)

    # pega dados que foram salvos em um arquivo
    def pega(self, nomeArquivo):
        self.criaDiretorio()
        nomeArquivo = f'{nomeArquivo}.json'
        caminho = self.diretorio + nomeArquivo

        try:
            with open(caminho, 'rb') as arquivo:
                itemlist = pickle.load(arquivo)
            return itemlist
        except EOFError:
            return None
        except:
            open(caminho, 'x')

    def criaDiretorio(self):
        if not os.path.exists(self.diretorio):
            os.makedirs(self.diretorio)

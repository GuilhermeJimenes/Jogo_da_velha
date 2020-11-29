class Inteligente:
    def __init__(self, inteligencia, entradas):
        self.IInteligencia = inteligencia
        self.IEntradas = entradas

    # define qual é a melhor jogada a se fazer pegando o menor score, feito isso
    # verifica quantos valores repetidos existem e pega qualquer um aleatoriamente
    # é essencial que seja aleatorizado para não criar um tendencia de jogadas
    def inteligenteJoga(self):
        from random import shuffle
        noh = self.IInteligencia.pegaQualquerNoh(umParaPegaScore=1)
        scores = noh['score']
        todosMenores = []

        for posicao, score in enumerate(scores):
            if score == min(scores):
                todosMenores.append(posicao)
        shuffle(todosMenores)
        jogada = todosMenores[0]
        return jogada

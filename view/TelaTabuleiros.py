import PySimpleGUI as sg


class TelaTabuleiros:
    def __init__(self):
        sg.change_look_and_feel('DarkBlue13')
        self.caixaTamanho = 165
        self.Janela = sg.Window('Jogo da velha', self.layout(), finalize=True, keep_on_top=True)
        self.Evento = None
        self.Valores = None
        self.Mouse = None
        self.LetraLocalizacao = None

    def layout(self):
        layout = [
            [sg.Graph((300, 300), (0, 500), (500, 0), key='-GRAPH-',
                      change_submits=True, drag_submits=False)]
        ]
        return layout

    def grafico(self):
        grafico = self.Janela['-GRAPH-']
        return grafico

    def tabuleiro(self):
        for linha in range(3):
            for coluna in range(3):
                self.grafico().draw_rectangle(
                    (coluna * self.caixaTamanho + 5, linha * self.caixaTamanho + 3),
                    (coluna * self.caixaTamanho + self.caixaTamanho + 5, linha *
                     self.caixaTamanho + self.caixaTamanho + 3),
                    line_color='black', fill_color='white'
                )
                # g.draw_text('{}'.format(row * 3 + col + 1),  # Numeração
                #             (col * caixaTamanho + 10, row * caixaTamanho + 8))

    def extrairDados(self, tempo):
        self.Evento, self.Valores = self.Janela.read(timeout=tempo)
        if self.Evento == sg.WIN_CLOSED:
            exit()
        self.Mouse = self.Valores['-GRAPH-']

    def popupGanhou(self, peca):
        sg.popup('Fim de jogo!', f'Jogador {peca} GANHOU!', keep_on_top=True)

    def popupVelha(self):
        sg.popup('Fim de jogo!', 'Deu EMPATE, ninguém ganhou!', keep_on_top=True)

    def jogadaInvalida(self):
        self.Evento, self.Valores = self.Janela.read()
        if self.Evento == sg.WIN_CLOSED:
            exit()
        else:
            self.Mouse = self.Valores['-GRAPH-']
            return self.insercaoClique()

    def insercaoClique(self):
        if self.Evento == '-GRAPH-':
            caixaX = self.Mouse[0] // self.caixaTamanho
            caixaY = self.Mouse[1] // self.caixaTamanho
            jogada = caixaY * 3 + caixaX
            self.LetraLocalizacao = (caixaX * self.caixaTamanho + 80, caixaY * self.caixaTamanho + 85)
            return jogada

    def preencherClique(self, peca):
        self.grafico().draw_text(f'{peca}', self.LetraLocalizacao, font='helvetica 80')

    def insercaoManual(self, jogada, peca):
        letraLocalizacao = ((jogada % 3) * self.caixaTamanho + 80, (jogada // 3) * self.caixaTamanho + 85)
        self.grafico().draw_text(f'{peca}', letraLocalizacao, font='helvetica 80')

    def limpaTabuleiro(self):
        self.Janela.find_element(key='-GRAPH-').Update(None)


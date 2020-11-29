import PySimpleGUI as sg


class TelaPreJogos:
    def __init__(self, getTodosTiposJogadores):
        sg.change_look_and_feel('lightGrey1')  # define tema de cores
        self.GetTodosTiposJogadores = getTodosTiposJogadores
        self.Valores = self.conteudo()

    # define tudo que vai estar na janela
    def layout(self):
        tiposJ = self.GetTodosTiposJogadores
        box1 = [[sg.Listbox([tiposJ[0], tiposJ[1], tiposJ[2], tiposJ[3]], key='player1', size=(15, 4))]]
        box2 = [[sg.Listbox([tiposJ[0], tiposJ[1], tiposJ[2], tiposJ[3]], key='player2', size=(15, 4))]]

        layout = [
            [sg.Text('Quantidade de partidas:', size=(9, 0)), sg.Input(size=(15, 0),
            key='partidas', tooltip='Valores abaixo de 1 seram considerados como 1')],

            [sg.TabGroup([[sg.Tab('Jogador 1', box1), sg.Tab('Jogador 2', box2)]])],

            [sg.Button('Ok', tooltip='Marque todos os campos'), sg.Button('Fechar')]
        ]
        return layout

    # cria janela
    def janela(self):
        janela = sg.Window('Configurações de partida', self.layout(), finalize=True, keep_on_top=True)
        return janela

    # Extrair os dados da tela
    def conteudo(self):
        while True:
            self.button, self.valores = self.janela().Read(close=True)
            if self.button in (None, 'Fechar'):  # Fecha a janela se clicar em cancelar
                exit()
            # impede que prossiga sem marcar todos os campos
            elif self.valores['partidas'] and self.valores['player1'] and self.valores['player2']:
                return self.valores

    def getValores(self):
        return self.Valores

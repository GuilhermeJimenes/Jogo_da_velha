class Dependencia:
    def __init__(self):
        self.IAtuadoreCtrl = None
        self.IBaseDeDadoCtrl = None
        self.IFimDeJogoCtrl = None
        self.IPecaCtrl = None
        self.IPreJogoCtrl = None

        self.IPreJogo = None
        self.ITabuleiroCtrl = None

        self.IAleatorioJogadas = None

        self.IDificilJogadas = None
        self.IDificilSensores = None

        self.IInteligente = None
        self.IInteligencia = None
        self.IConhecimento = None

        self.IAmbiente = None
        self.IAtuadore = None
        self.IArquivosExternos = None
        self.IFimDeJogo = None
        self.IPartidas = None
        self.IPerformances = None
        self.ISensore = None
        self.IEntrada = None
        self.IDadosFixos = None

        self.ITelaPreJogo = None
        self.ITelaTabuleiro = None

    # ------------------------ CONTROLLER ------------------------

    # agente inteligente

    #

    def atuadoresCtrl(self):
        from controller.AtuadoresCtrl import AtuadoresCtrl
        if self.IAtuadoreCtrl is None:
            self.IAtuadoreCtrl = AtuadoresCtrl(self.atuadores(), self.preJogosCtrl())
        return self.IAtuadoreCtrl

    def baseDeDadosCtrl(self):
        from controller.BaseDeDadosCtrl import BaseDeDadosCtrl
        if self.IBaseDeDadoCtrl is None:
            self.IBaseDeDadoCtrl = BaseDeDadosCtrl(
                self.ambientes(), self.arquivosExternos(),
                self.dadosFixos().nomeArquivoIA(), self.inteligencia())
        return self.IBaseDeDadoCtrl

    def fimDeJogosCtrl(self):
        from controller.FimDeJogosCtrl import FimDeJogosCtrl
        if self.IFimDeJogoCtrl is None:
            self.IFimDeJogoCtrl = FimDeJogosCtrl(
                self.preJogosCtrl(), self.telaTabuleiros(),
                self.fimDeJogos(), self.baseDeDadosCtrl(),
                self.dadosFixos().getTodosTiposJogadores(),
                self.performances(), self.inteligencia(),
                self.entradas(), self.partidas()
            )
        return self.IFimDeJogoCtrl

    def pecasCtrl(self):
        from controller.PecasCtrl import PecasCtrl
        if self.IPecaCtrl is None:
            self.IPecaCtrl = PecasCtrl(self.sensores(), self.dadosFixos())
        return self.IPecaCtrl

    def preJogosCtrl(self):
        from controller.PreJogosCtrl import PreJogosCtrl
        if self.IPreJogoCtrl is None:
            self.IPreJogoCtrl = PreJogosCtrl(self.sensores(), self.preJogos(), self.dadosFixos())
        return self.IPreJogoCtrl

    #

    def preJogos(self):
        from model.PreJogos import PreJogos
        if self.IPreJogo is None:
            self.IPreJogo = PreJogos(self.telaPreJogos().getValores())
        return self.IPreJogo

    def tabuleirosCtrl(self):
        from controller.TabuleirosCtrl import TabuleiroCtrl
        if self.ITabuleiroCtrl is None:
            self.ITabuleiroCtrl = TabuleiroCtrl(
                self.ambientes(), self.entradas(), self.preJogos(),
                self.inteligencia(), self.telaTabuleiros(),
                self.preJogosCtrl(), self.fimDeJogosCtrl(),
                self.pecasCtrl(), self.atuadoresCtrl(),
                self.dadosFixos().getTodosTiposJogadores(),
            )
        return self.ITabuleiroCtrl

    # ------------------------ MODEL ------------------------

    # agente aleatorio

    def aleatorioJogadas(self):
        from model.agenteAleatorio.AleatorioJogadas import AleatorioJogadas
        if self.IAleatorioJogadas is None:
            self.IAleatorioJogadas = AleatorioJogadas(self.entradas())
        return self.IAleatorioJogadas

    # agente dificil

    def dificilJogadas(self):
        from model.agenteDificil.DificilJogadas import DificilJogadas
        if self.IDificilJogadas is None:
            self.IDificilJogadas = DificilJogadas(
                self.ambientes(), self.entradas(), self.dificilSensores(),
                self.dadosFixos().getJogadorUmPeca(), self.dadosFixos().simboloCampoVazio()
            )
        return self.IDificilJogadas

    def dificilSensores(self):
        from model.agenteDificil.DificilSensores import DificilSensores
        if self.IDificilSensores is None:
            self.IDificilSensores = DificilSensores(
                self.sensores(), self.aleatorioJogadas(), self.dadosFixos().getTodasPecas()
            )
        return self.IDificilSensores

    # agente inteligente

    def inteligente(self):
        from model.agenteInteligente.Inteligente import Inteligente
        if self.IInteligente is None:
            self.IInteligente = Inteligente(self.inteligencia(), self.entradas())
        return self.IInteligente

    def inteligencia(self):
        from model.agenteInteligente.Inteligencia import Inteligencia
        if self.IInteligencia is None:
            self.IInteligencia = Inteligencia(
                self.dadosFixos().nomeArquivoIA(), self.arquivosExternos(),
                self.ambientes(), self.entradas(), self.dadosFixos().getTodosTiposJogadores(),
                self.preJogos(), self.partidas())
        return self.IInteligencia

    def ambientes(self):
        from model.Ambientes import Ambientes
        if self.IAmbiente is None:
            self.IAmbiente = Ambientes()
        return self.IAmbiente

    def atuadores(self):
        from model.Atuadores import Atuadores
        if self.IAtuadore is None:
            self.IAtuadore = Atuadores(
                self.aleatorioJogadas(), self.dificilJogadas(),
                self.dadosFixos().getTodosTiposJogadores(), self.inteligente())
        return self.IAtuadore

    def arquivosExternos(self):
        from model.ArquivosExternos import ArquivosExternos
        if self.IArquivosExternos is None:
            self.IArquivosExternos = ArquivosExternos()
        return self.IArquivosExternos

    def entradas(self):
        from model.Entradas import Entradas
        if self.IEntrada is None:
            self.IEntrada = Entradas(
                self.ambientes(), self.dadosFixos().simboloCampoVazio())
        return self.IEntrada

    def fimDeJogos(self):
        from model.FimDeJogos import FimDeJogos
        if self.IFimDeJogo is None:
            self.IFimDeJogo = FimDeJogos(
                self.ambientes(), self.dadosFixos().simboloCampoVazio())
        return self.IFimDeJogo

    def partidas(self):
        from model.Partidas import Partidas
        if self.IPartidas is None:
            self.IPartidas = Partidas()
        return self.IPartidas

    def performances(self):
        from model.Performances import Performances
        if self.IPerformances is None:
            self.IPerformances = Performances(
                self.preJogos(), self.dadosFixos().nomeArquivoPerformance(),
                self.arquivosExternos(), self.dadosFixos().getTodasPecas())
        return self.IPerformances

    def sensores(self):
        from model.Sensores import Sensores
        if self.ISensore is None:
            self.ISensore = Sensores(
                self.ambientes(), self.dadosFixos().simboloCampoVazio(),
                self.dadosFixos().getTodasPecas())
        return self.ISensore

    def dadosFixos(self):
        from model.DadosFixos import DadosFixos
        if self.IDadosFixos is None:
            self.IDadosFixos = DadosFixos()
        return self.IDadosFixos

    # ------------------------ VIEW ------------------------

    def telaPreJogos(self):
        from view.TelaPreJogos import TelaPreJogos
        if self.ITelaPreJogo is None:
            self.ITelaPreJogo = TelaPreJogos(self.dadosFixos().getTodosTiposJogadores())
        return self.ITelaPreJogo

    def telaTabuleiros(self):
        from view.TelaTabuleiros import TelaTabuleiros
        if self.ITelaTabuleiro is None:
            self.ITelaTabuleiro = TelaTabuleiros()
        return self.ITelaTabuleiro

    # ------------------------ auxiliares ------------------------

    # limpa todas as instancias criadas
    def apagaObjetos(self):
        self.IAtuadoreCtrl = None
        self.IBaseDeDadoCtrl = None
        self.IFimDeJogoCtrl = None
        self.IPecaCtrl = None
        self.IPreJogoCtrl = None

        self.IPreJogo = None
        self.ITabuleiroCtrl = None

        self.IAleatorioJogadas = None

        self.IDificilJogadas = None
        self.IDificilSensores = None

        self.IInteligente = None
        self.IInteligencia = None
        self.IConhecimento = None

        self.IAmbiente = None
        self.IAtuadore = None
        self.IArquivosExternos = None
        self.IFimDeJogo = None
        # self.IPartidas = None
        # self.IPerformances = None
        self.ISensore = None
        self.IEntrada = None
        self.IDadosFixos = None

        # self.ITelaPreJogo = None # As configuração PreJogo devem ser mantidas
        # self.ITelaTabuleiro = None # Está sendo limpo no metodo limpaTabuleiro

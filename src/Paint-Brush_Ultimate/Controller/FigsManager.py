import Model.FigsDef as fd
class MenegFig:

    def __init__(self):
        self.figuras = []
        self.selecionada = None

    def selecionar(self, x, y):

        self.selecionada = None

        for figura in reversed(self.figuras):
            if figura.foiClick(x, y):
                self.selecionada = figura
                return figura

        return None
    

manager = MenegFig()
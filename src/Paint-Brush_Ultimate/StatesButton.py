import FigsDef as figs

class StatesANDassembler:
    def __init__(self, currentState):
        self.currentState = currentState

        self.stateDict = {
            "retangulo": figs.Retangulo(),
            "circulo": figs.Circulo(),
            "linha": figs.Linha(),
            "maoLivre": figs.MaoLivre()
        }
    
    def BuildFigure(self, estado, Xi,Yi, Xf,Yf, canvas):
        self.stateDict[estado].draw(Xi, Yi, Xf, Yf, canvas)
    
    def switchState(self, estado):
        self.currentState = estado

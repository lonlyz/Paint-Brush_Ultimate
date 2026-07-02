import Model.FigsDef as figs

class StateMachine:
    def __init__(self, currentState):
        self.currentState = currentState
    
    
    def switchState(self, estado):
        self.currentState = estado


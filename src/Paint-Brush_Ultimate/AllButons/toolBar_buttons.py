#Arquivo apenas para gerir os botões do toolbar

from figures import Figuras as Figs

class Freehand(Figs):
    def __init__(self, positionButton, skin):
        self.positionButton = positionButton
        self.skin = skin

    def draw(self):
        pass

class Rectangle(Figs):
    pass

class Oval(Figs):
    pass

class Line(Figs):
    pass

class Eraser(Figs):
    pass
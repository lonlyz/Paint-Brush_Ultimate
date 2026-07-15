import json
from tkinter import filedialog

#Arquivo responsável pela gestão do salvamento e importação de alterações

class SaveAndLoad:  
    def __init__(self, canvasObj):

        self.coordEcores = {
            """Cada atributo deste objeto corresponde as posições e cores dos desenhos feitos"""

            "DrawsRet": canvasObj.stateDict["retangulo"].arrayDraws,
            "DrawsOval": canvasObj.stateDict["circulo"].arrayDraws,
            "DrawsLinha": canvasObj.stateDict["linha"].arrayDraws,
            "DrawsMao": canvasObj.stateDict["maoLivre"].arrayDraws,
            "DrawsPoly": canvasObj.stateDict["poligono"].arrayDraws,
            "DrawsArco": canvasObj.stateDict["arco"].arrayDraws
        }

    def save(self):
        pasta = filedialog.askdirectory()
        print(pasta)

        if pasta:
            pass

    def load(self):
        pass
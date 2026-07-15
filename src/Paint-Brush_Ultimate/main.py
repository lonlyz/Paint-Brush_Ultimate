import tkinter as tk
from View import elements as Elm
import Controller.StatesButton as Stb
from Model import JsonManager as Js

class Interface:
    def __init__(self):

        #Interface Tk e título de cabeçalho
        self.janela = tk.Tk()
        self.janela.title("Paint Brush - Ultimate")
        
        #Máquina de estados
        self.statemachine = Stb.StateMachine("maoLivre")

        #Barra de ferramentas e do canvas
        self.toolbar = Elm.Toolbar(self.janela, tk, self.statemachine) 
        self.canvas = Elm.Canvas(self.janela, tk, self.statemachine, self.toolbar)
        
        #Gerenciamento do json e do header
        self.jsonProcess = Js.SaveAndLoad(self.canvas)
        self.header = Elm.header(self.janela, tk, self.statemachine, self.jsonProcess)
        
        self.janela.mainloop()

interface = Interface()

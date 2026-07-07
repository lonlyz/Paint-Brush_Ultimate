import tkinter as tk
import elements as Elm
import Controller.StatesButton as Stb

class Interface:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Paint Brush - Ultimate")
        
        self.statemachine = Stb.StateMachine("maoLivre")

        self.toolbar = Elm.Toolbar(self.janela, tk, self.statemachine)    
        self.canvas = Elm.Canvas(self.janela, tk, self.statemachine, self.toolbar)
        
        
        self.janela.mainloop()

interface = Interface()

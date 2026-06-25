#Arquivo que gerencia todos os processos

import tkinter as tk
import botoesfunc as btf
from sections import ToolBar,Header,TeladPintura

class Interface:
    """Classe para a interface em si"""

    def __init__(self):
        self.janela = tk.Tk()

        self.toolBar = ToolBar(self.janela)
        self.header = Header(self.janela)
        self.canvas = TeladPintura(self.janela)

        self.tela_configs()
        self.frames()

        self.janela.mainloop()
    
    def tela_configs(self):
        self.janela.title("Bem Vindo ao Paint Brush Ultimate | clique e arraste para desenhar")
        self.janela.geometry("1280x720")
        self.janela.title("Janela main")
        self.janela.resizable(False,False)
    
    def frames(self):
        self.frame_toolBar = Frame(self.janela)
        self.frame.place(relx = 0.1, rely = 1, relwidth = 0.3, relheight = 1)

Interface()


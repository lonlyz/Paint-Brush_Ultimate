import Model.FigsDef as figs
from tkinter import colorchooser

class Toolbar:
    def __init__(self, window, mod, stateObj):
        self.ref = mod
        self.janela = window
        
        self.frame = mod.Frame(self.janela, bg='#31487A', width=150)
        self.frame.pack(side="left", fill="y", padx=10, pady=10)
        self.cor_atual = "black"

        self.ref.Button(self.frame, text="Mão Livre", command=lambda: stateObj.switchState("maoLivre")).pack(side="top", fill="x", pady=5, padx=5)
        self.ref.Button(self.frame, text="Retângulo", command=lambda: stateObj.switchState("retangulo")).pack(side="top", fill="x", pady=5, padx=5)
        self.ref.Button(self.frame, text="Círculo", command=lambda: stateObj.switchState("circulo")).pack(side="top", fill="x", pady=5, padx=5)
        self.ref.Button(self.frame, text="Linha", command=lambda: stateObj.switchState("linha")).pack(side="top", fill="x", pady=5, padx=5)
        self.ref.Button(self.frame, text="Polígono", command=lambda: stateObj.switchState("poligono")).pack(side="top", fill="x", pady=5, padx=5)
        self.ref.Button(self.frame, text="Arco", command=lambda: stateObj.switchState("arco")).pack(side="top", fill="x", pady=5, padx=5)

        self.btn_cor = self.ref.Button(
            self.frame, 
            text="Selecionar Cor", 
            bg=self.cor_atual, 
            fg="white", 
            command=self.escolher_cor
        )
        self.btn_cor.pack(side="bottom", fill="x", pady=15, padx=5)

    def escolher_cor(self):
       
        cor = colorchooser.askcolor(title="Escolha uma cor para desenhar")
        
        if cor[1]: 
            self.cor_atual = cor[1]
            self.btn_cor.config(bg=self.cor_atual)

class Canvas:
    def __init__(self, window, mod, stateObj, toolbarObj):
        self.stateObj = stateObj
        self.toolbarObj = toolbarObj
        self.janela = window
        self.canvas = mod.Canvas(self.janela, width=800, height=800, bg='white')
        self.canvas.pack(side="left", expand=True, fill="both", padx=10, pady=10)

        # Estados das ferramentas usadas no canvas
        self.stateDict = {
            "retangulo": figs.Retangulo(self.canvas),
            "circulo": figs.Oval(self.canvas),
            "linha": figs.Linha(self.canvas),
            "maoLivre": figs.MaoLivre(self.canvas),
            "poligono": figs.Poligono(self.canvas), 
            "arco": figs.Arco(self.canvas)
        }      

        self.canvas.bind('<B1-Motion>', self.Create)
        self.canvas.bind('<Button-1>', self.MarcaInicio)

    def Create(self, event):
        cor = self.toolbarObj.cor_atual
        self.stateDict[self.stateObj.currentState].draw(event, cor)

    def MarcaInicio(self, event):
         self.stateDict[self.stateObj.currentState].marca_inicio(event)
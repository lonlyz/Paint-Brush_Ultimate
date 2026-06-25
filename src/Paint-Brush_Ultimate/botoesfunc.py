import tkinter as tk
from tkinter import colorchooser
class botoes:

    def __init__(self,conteiner):

        self.frame = tk.Frame(
        conteiner,
        bg="white",
        width=200,
        height=500,
        relief="raised"
    )

        self.frame.pack(side="left", fill="y",)
        self.frame.pack_propagate(True)

        # botoes de opções  

        self.forma = "linha" # < forma padrão

        retanguloButon = tk.Button(
            self.frame,
            text="Retângulo",
            command=lambda: self.selecionar_forma("retangulo")
        )
        retanguloButon.pack(pady=10)

        circuloButon = tk.Button(
            self.frame,
            text="Círculo",
            command=lambda: self.selecionar_forma("circulo")
        )
        circuloButon.pack(pady=10)

        linhaButon = tk.Button(
            self.frame, 
            text="linha",
            command=lambda: self.selecionar_forma("linha")
        )
        linhaButon.pack(pady=10)

        separador = tk.Label(self.frame, text="cores") # < uma faixa para separar as cores das formas 
        separador.pack(pady=5,fill="x")

        # cores

        self.cor = "Black" # < cor padrão


        botaoMultcor = tk.Button(
            self.frame,
            command=self.escolher_cor,
            text="cor",
            height=1,
            width=2,
            relief="solid"
        )
        botaoMultcor.pack(pady=5)
       


    # funçoes operacionais   :)
        
    def seleciona_cor(self,cor):
        self.cor = cor
        #print(cor) # somente para testes

    def selecionar_forma(self,forma):
        self.forma = forma
        #print(forma) # somente para testes

    def escolher_cor(self):

        cor_selecionada = colorchooser.askcolor(title="Escolha uma cor")

        if cor_selecionada[1] is not None:
           self.cor = cor_selecionada[1]
  
        

    


    

      


       









  
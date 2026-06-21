import tkinter as tk

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

        corVermelho = tk.Button(
            self.frame,
            bg="red",
            height=1,
            width=2, 
            bd=2,
            relief="raised",
            command=lambda: self.seleciona_cor("red")
        )
        corVermelho.pack(pady=5)

        corVerde = tk.Button(
            self.frame,
            bg="green",
            height=1,
            width=2,
            bd = 2,
            relief="raised",
            command=lambda: self.seleciona_cor("green")
        )
        corVerde.pack(pady=5)

        corAzul = tk.Button(
            self.frame,
            bg="blue",
            height=1,
            width=2,
            bd = 2,
            relief="raised",
            command=lambda: self.seleciona_cor("blue")
        )
        corAzul.pack(pady=5)

        corAmarelo = tk.Button(
            self.frame,
            bg="yellow",
            height=1,
            width=2,
            bd = 2,
            relief="raised",
            command=lambda: self.seleciona_cor("yellow")
        )
        corAmarelo.pack(pady=5)
        
        corRosa = tk.Button(
            self.frame,
            bg="pink",
            height=1,
            width=2,
            bd = 2,
            relief="raised",
            command=lambda: self.seleciona_cor("pink")
        )
        corRosa.pack(pady=5)

        corPreto = tk.Button(
            self.frame,
            bg="black",
            height=1,
            width=2,
            bd = 2,
            relief="raised",
            command=lambda: self.seleciona_cor("black")

        )
        corPreto.pack(pady=5)

    # funçoes operacionais   :)
        
    def seleciona_cor(self,cor):
        self.cor = cor
        #print(cor) # somente para testes

    def selecionar_forma(self,forma):
        self.forma = forma
        #print(forma) # somente para testes
        

    


    

      


       









  
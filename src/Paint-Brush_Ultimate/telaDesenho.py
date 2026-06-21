import tkinter as tk
import botoesfunc as btf

# para executar esse programa, execute o telaPrincipal
class telaDdesenho: 

    def __init__(self,conteiner,botoes):

        #UI

        self.botoes = botoes

        self.frame = tk.Frame( # inicializa o frame da tela
            conteiner,
            
        )

        self.botoes = botoes

        self.frame.pack()
        self.frame.pack_propagate(True)

        self.canvas = tk.Canvas(
            self.frame,
            bg="white",
            height=800,
            width=600,

        )

        self.canvas.pack(anchor="center")
        
        # desenha

        self.ini_x = None
        self.ini_y = None

        self.canvas.bind('<ButtonPress-1>', self.marca_inicio)
        self.canvas.bind('<B1-Motion>', self.atualiza_fim)

    def marca_inicio(self, event):
        
        self.ini_x = event.x
        self.ini_y = event.y

    def atualiza_fim(self, event): 
        fim_x = event.x
        fim_y = event.y
        self.canvas.delete("all") # < comente isso e embarque na doideira kkk

        match self.botoes.forma:

            case "retangulo":
                self.canvas.create_rectangle(
                    self.ini_x,
                    self.ini_y,
                    fim_x,
                    fim_y,
                    fill=self.botoes.cor
                )

            case "circulo":
                self.canvas.create_oval(
                    self.ini_x,
                    self.ini_y,
                    fim_x,
                    fim_y,
                    fill=self.botoes.cor
                )
            
            case "linha":
                self.canvas.create_line(
                    self.ini_x,
                    self.ini_y,
                    fim_x,
                    fim_y,
                    fill=self.botoes.cor  
                )

            case _:
                self.canvas.create_line(
                    self.ini_x,
                    self.ini_y,
                    fim_x,
                    fim_y,
                    fill=self.botoes.cor
                )

    
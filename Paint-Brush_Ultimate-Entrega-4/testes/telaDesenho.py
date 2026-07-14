import tkinter as tk

# para executar esse programa, execute o telaPrincipal
class telaDdesenho: 

    def __init__(self,conteiner):

        self.frame = tk.Frame( # inicializa o frame da tela
            conteiner,
            
        )

        self.frame.pack()

        self.canvas = tk.Canvas(
            self.frame,
            bg="white",
            height=800,
            width=600,

        )

        self.canvas.pack()

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
        self.canvas.delete("all")

        self.canvas.create_rectangle(
            self.ini_x,
            self.ini_y,
            fim_x,
            fim_y,
            fill='pink', # cor interna
            outline='blue' # cor da bora 
        )
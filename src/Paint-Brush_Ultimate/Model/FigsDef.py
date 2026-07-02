from Controller.figures import Figuras

class Retangulo(Figuras):
    def __init__(self, canvas):
        self.tela = canvas
        self.ini_x = self.ini_y = self.fim_x = self.fim_y = 0
        
    def marca_inicio(self, event):
        self.ini_x = event.x
        self.ini_y = event.y

    def draw(self, event, cor):
        self.fim_x = event.x
        self.fim_y = event.y
        self.tela.delete("preview")
        self.tela.create_rectangle(self.ini_x, self.ini_y, self.fim_x, self.fim_y, tags="preview", fill=cor)

class Oval(Figuras):
    def __init__(self, canvas):
        self.tela = canvas
        self.ini_x = self.ini_y = self.fim_x = self.fim_y = 0
        
    def marca_inicio(self, event):
        self.ini_x = event.x
        self.ini_y = event.y

    def draw(self, event, cor):
        self.fim_x = event.x
        self.fim_y = event.y
        self.tela.delete("preview")
        self.tela.create_oval(self.ini_x, self.ini_y, self.fim_x, self.fim_y, tags="preview", fill=cor)

class Linha(Figuras):
    def __init__(self, canvas):
        self.tela = canvas
        self.ini_x = self.ini_y = self.fim_x = self.fim_y = 0
        
    def marca_inicio(self, event):
        self.ini_x = event.x
        self.ini_y = event.y

    def draw(self, event, cor):
        self.fim_x = event.x
        self.fim_y = event.y
        self.tela.delete("preview") 
        self.tela.create_line(self.ini_x, self.ini_y, self.fim_x, self.fim_y, tags="preview", fill=cor)

class Poligono(Figuras):
    def __init__(self, canvas):
        self.tela = canvas
        self.ini_x = self.ini_y = self.fim_x = self.fim_y = 0
        
    def marca_inicio(self, event):
        self.ini_x = event.x
        self.ini_y = event.y

    def draw(self, event, cor):
        self.fim_x = event.x
        self.fim_y = event.y
        self.tela.delete("preview") 
        
        ponto3_x = self.ini_x - (self.fim_x - self.ini_x)
        
        self.tela.create_polygon(
            self.ini_x, self.ini_y, 
            self.fim_x, self.fim_y, 
            ponto3_x, self.fim_y, 
            tags="preview", fill=cor, outline="black"
        )


class Arco(Figuras):
    def __init__(self, canvas):
        self.tela = canvas
        self.ini_x = self.ini_y = self.fim_x = self.fim_y = 0

    def marca_inicio(self, event):
        self.ini_x = event.x
        self.ini_y = event.y

    def draw(self, event, cor):
        self.fim_x = event.x
        self.fim_y = event.y
        self.tela.delete("preview")
        self.tela.create_arc(self.ini_x, self.ini_y, self.fim_x, self.fim_y, fill=cor,tags="preview", style="arc")

class MaoLivre(Figuras):
    def __init__(self, canvas):
        self.tela = canvas
        self.ini_x = self.ini_y = 0
        

    def marca_inicio(self, event):
        self.ini_x = event.x
        self.ini_y = event.y

    def draw(self, event, cor):
    
        self.tela.create_line(self.ini_x, self.ini_y, event.x, event.y, capstyle="round", smooth=True, fill=cor,width=2)
        
        self.ini_x = event.x
        self.ini_y = event.y
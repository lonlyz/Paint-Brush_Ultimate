from Controller.figures import Figuras
import Controller.FigsManager as fgm

class FiguraRetangulo:

    def __init__(self, x1, y1, x2, y2, cor):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.cor = cor
   
    def __repr__(self):
        
        return ( f"Retangulo({self.x1}, {self.y1}, "f"{self.x2}, {self.y2}, {self.cor})")
        

    def foiClick(self,x,y):

        xMim = min(self.x1,self.x2)
        xmax = max(self.x1,self.x2)

        ymin = min(self.y1,self.y2)
        ymax = max(self.y1,self.y2)

        return xMim <= x <= xmax and ymin <= y <= ymax

    
class Retangulo(Figuras):
    def __init__(self, canvas):
        self.tela = canvas
        self.ini_x = self.ini_y = self.fim_x = self.fim_y = 0
        self.drawsFinish = 0 
        self.arrayDraws = [] # da erro quando eu apago

    def marca_inicio(self, event):
        self.ini_x = event.x
        self.ini_y = event.y
        self.drawsFinish += 1

    def draw(self, event, cor):
        self.fim_x = event.x
        self.fim_y = event.y
        self.tela.delete(str(self.drawsFinish) + "rectangle")
        self.tela.create_rectangle(
            self.ini_x, self.ini_y, 
            self.fim_x, self.fim_y, 
            tags=str(self.drawsFinish) + "rectangle", 
            fill=cor
        )

    def saveToArray(self, event, cor):

        self.fim_x = event.x
        self.fim_y = event.y

        figura = FiguraRetangulo(
            self.ini_x,
            self.ini_y,
            self.fim_x,
            self.fim_y,
            cor
        )

        fgm.manager.figuras.append(figura)

        print("Figura adicionada:")
        print(figura)

        print("\nTodas as figuras:")

        for fig in fgm.manager.figuras:
            print(fig)

class figuraOval:
    def __init__(self, x1, y1, x2, y2, cor):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.cor = cor
   
    def __repr__(self):
        
        return ( f"Oval({self.x1}, {self.y1}, "f"{self.x2}, {self.y2}, {self.cor})")
    
    
    def foiClick(self,x,y):

        xMim = min(self.x1,self.x2)
        xmax = max(self.x1,self.x2)

        ymin = min(self.y1,self.y2)
        ymax = max(self.y1,self.y2)

        return xMim <= x <= xmax and ymin <= y <= ymax

class Oval(Figuras):
    def __init__(self, canvas):
        self.tela = canvas
        self.ini_x = self.ini_y = self.fim_x = self.fim_y = 0
        self.drawsFinish = 0 
        self.arrayDraws = [] 

    def marca_inicio(self, event):
        self.ini_x = event.x
        self.ini_y = event.y
        self.drawsFinish += 1

    def draw(self, event, cor):
        self.fim_x = event.x
        self.fim_y = event.y
        self.tela.delete(str(self.drawsFinish) + "oval")
        self.tela.create_oval(
            self.ini_x, self.ini_y, 
            self.fim_x, self.fim_y, 
            tags=str(self.drawsFinish) + "oval", 
            fill=cor
        )

    def saveToArray(self, event,cor):

        self.fim_x = event.x
        self.fim_y = event.y

        figura =  figuraOval(
            self.ini_x,
            self.ini_y,
            self.fim_x,
            self.fim_y,
            cor
        )

        fgm.manager.figuras.append(figura)

        print("Figura adicionada:")
        print(figura)

        print("\nTodas as figuras:")

        for fig in fgm.manager.figuras:
            print(fig)
       
       
class figuraLinha:
    def __init__(self, x1, y1, x2, y2, cor):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.cor = cor
   
    def __repr__(self):
        
        return ( f"linha({self.x1}, {self.y1}, "f"{self.x2}, {self.y2}, {self.cor})")
    
    
    def foiClick(self,x,y):

        xMim = min(self.x1,self.x2)
        xmax = max(self.x1,self.x2)

        ymin = min(self.y1,self.y2)
        ymax = max(self.y1,self.y2)

        return xMim <= x <= xmax and ymin <= y <= ymax


class Linha(Figuras):
    def __init__(self, canvas):
        self.tela = canvas
        self.ini_x = self.ini_y = self.fim_x = self.fim_y = 0
        self.drawsFinish = 0
        self.arrayDraws = [] 
        
    def marca_inicio(self, event):
        self.ini_x = event.x
        self.ini_y = event.y
        self.drawsFinish += 1

    def draw(self, event, cor):
        self.fim_x = event.x
        self.fim_y = event.y
        self.tela.delete(str(self.drawsFinish) + "linha") 
        self.tela.create_line(
            self.ini_x, self.ini_y, 
            self.fim_x, self.fim_y, 
            tags=str(self.drawsFinish) + "linha", 
            fill=cor
        )

    def saveToArray(self, event,cor):

        self.fim_x = event.x
        self.fim_y = event.y

        figura =  figuraLinha(
            self.ini_x,
            self.ini_y,
            self.fim_x,
            self.fim_y,
            cor
        )

        fgm.manager.figuras.append(figura)

        print("Figura adicionada:")
        print(figura)

        print("\nTodas as figuras:")

        for fig in fgm.manager.figuras:
            print(fig)

class figuraPoligono:
    def __init__(self, x1, y1, x2, y2,x3,y3, cor):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.cor = cor
   
    def __repr__(self):
        
        return ( f"poligono({self.x1}, {self.y1}, "f"{self.x2}, {self.y2},{self.x3},{self.y3} {self.cor})")
    
    
    def foiClick(self,x,y):

        xMim = min(self.x1,self.x2,self.x3)
        xmax = max(self.x1,self.x2,self.x3)

        ymin = min(self.y1,self.y2,self.y3)
        ymax = max(self.y1,self.y2,self.y3)

        return xMim <= x <= xmax and ymin <= y <= ymax

       

class Poligono(Figuras):
    def __init__(self, canvas):
        self.tela = canvas
        self.ini_x = self.ini_y = self.fim_x = self.fim_y = 0
        self.drawsFinish = 0
        self.arrayDraws = []
        
    def marca_inicio(self, event):
        self.ini_x = event.x
        self.ini_y = event.y
        self.drawsFinish += 1

    def draw(self, event, cor):
        self.fim_x = event.x
        self.fim_y = event.y
        self.tela.delete(str(self.drawsFinish) + "polygon") 
        
        ponto3_x = self.ini_x - (self.fim_x - self.ini_x)
        
        self.tela.create_polygon(
            self.ini_x, self.ini_y, 
            self.fim_x, self.fim_y, 
            ponto3_x, self.fim_y, 
            tags=str(self.drawsFinish) + "polygon", 
            fill=cor, 
            outline="black"
        )

    def saveToArray(self, event,cor):
        self.fim_x = event.x
        self.fim_y = event.y
        ponto3_x = self.ini_x - (self.fim_x - self.ini_x)
        
        figura = figuraPoligono( self.ini_x, self.ini_y, 
            self.fim_x, self.fim_y, 
            ponto3_x, self.fim_y,cor)
        
        fgm.manager.figuras.append(figura)

        print("Figura adicionada:")
        print(figura)

        print("\nTodas as figuras:")

        for fig in fgm.manager.figuras:

            print(fig)
     
class figuraArco:
    def __init__(self, x1, y1, x2, y2, cor):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.cor = cor
   
    def __repr__(self):
        
        return ( f"arco({self.x1}, {self.y1}, "f"{self.x2}, {self.y2}, {self.cor})")
    
    
    def foiClick(self,x,y):

        xMim = min(self.x1,self.x2)
        xmax = max(self.x1,self.x2)

        ymin = min(self.y1,self.y2)
        ymax = max(self.y1,self.y2)

        return xMim <= x <= xmax and ymin <= y <= ymax

class Arco(Figuras):
    def __init__(self, canvas):
        self.tela = canvas
        self.ini_x = self.ini_y = self.fim_x = self.fim_y = 0
        self.drawsFinish = 0
        self.arrayDraws = []

    def marca_inicio(self, event):
        self.ini_x = event.x
        self.ini_y = event.y
        self.drawsFinish += 1

    def draw(self, event, cor):
        self.fim_x = event.x
        self.fim_y = event.y
        self.tela.delete(str(self.drawsFinish) + "arc")
        self.tela.create_arc(
            self.ini_x, self.ini_y, 
            self.fim_x, self.fim_y, 
            fill=cor, 
            tags=str(self.drawsFinish) + "arc", 
            style="arc"
        )

    def saveToArray(self, event,cor):

        self.fim_x = event.x
        self.fim_y = event.y

        figura =  figuraArco(
            self.ini_x,
            self.ini_y,
            self.fim_x,
            self.fim_y,
            cor
        )

        fgm.manager.figuras.append(figura)

        print("Figura adicionada:")
        print(figura)

        print("\nTodas as figuras:")

        for fig in fgm.manager.figuras:
            print(fig)


class MaoLivre(Figuras):
    def __init__(self, canvas):
        self.tela = canvas
        self.ini_x = self.ini_y = 0
        self.caminho_atual = [] 
        self.arrayDraws = [] 

    def marca_inicio(self, event):
        self.ini_x = event.x
        self.ini_y = event.y
        self.caminho_atual = [(self.ini_x, self.ini_y)]

    def draw(self, event, cor):
        self.tela.create_line(
            self.ini_x, self.ini_y, 
            event.x, event.y, 
            capstyle="round", smooth=True, fill=cor, width=2
        )
        self.ini_x = event.x
        self.ini_y = event.y
        self.caminho_atual.append((self.ini_x, self.ini_y))

    def saveToArray(self, event,cor):
        self.arrayDraws.append({"pontos":list(self.caminho_atual),"cor":cor})
        self.caminho_atual.clear()
        print("Mão livre salva! Todos os traços:", self.arrayDraws)
        fgm.manager.ListFig_Global["arco"].append({"pontos": self.caminho_atual, "Cor": cor})

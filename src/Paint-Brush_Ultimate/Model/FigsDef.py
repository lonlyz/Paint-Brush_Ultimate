from Controller.figures import Figuras

class Retangulo(Figuras):
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
        Retangulo_cordenadas = [self.ini_x, self.ini_y, self.fim_x, self.fim_y, cor]
        self.arrayDraws.append({"pontos":Retangulo_cordenadas,"Cor":cor})
        print("Retângulos salvos!:", self.arrayDraws)

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
        Oval_cordenadas = [self.ini_x, self.ini_y, self.fim_x, self.fim_y]
        self.arrayDraws.append({"pontos":Oval_cordenadas,"cor":cor})
        print("Ovais salvas!:", self.arrayDraws)


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

        linha_Cordenada = [self.ini_x, self.ini_y, self.fim_x, self.fim_y]
        self.arrayDraws.append({"Pontos":linha_Cordenada,"cor":cor})
        print("Linhas salvas!:", self.arrayDraws)


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
        
        
        triangulo_final = [
            self.ini_x, self.ini_y, 
            self.fim_x, self.fim_y, 
            ponto3_x, self.fim_y
        ]
        self.arrayDraws.append({"Pontos":triangulo_final,"cor":cor})
        print("Polígonos salvos!:", self.arrayDraws)


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
        self.arrayDraws.append({"Pontos":[self.ini_x, self.ini_y, self.fim_x, self.fim_y],"cor":cor})
        print("Arcos salvos!:", self.arrayDraws)


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

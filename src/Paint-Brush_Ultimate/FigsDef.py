from figures import Figuras


class Retangulo(Figuras):

    def draw(self, Xi, Yi, Xf, Yf, canvas):
        canvas.create_rectangle(Xi, Yi, Xf, Yf)


class Circulo(Figuras):

    def draw(self, Xi, Yi, Xf, Yf, canvas):
        canvas.create_oval(Xi, Yi, Xf, Yf)



class Linha(Figuras):

    def draw(self, Xi, Yi, Xf, Yf, canvas):
        canvas.create_line(Xi, Yi, Xf, Yf)


#class MaoLivre(Figuras):

#    def draw(self, Xi, Yi, Xf, Yf, canvas):
#        pass
from abc import ABC, abstractmethod

class Figuras(ABC):
    @abstractmethod    
    def draw(self, Xinicial, Yinicial, Xfinal, Yfinal, tela):
        pass 
from abc import ABC, abstractmethod

class Figuras(ABC):
    """Classe abstrata para as figuras"""
    @abstractmethod
    def marca_inicio(self, event):
        pass
    @abstractmethod
    def draw(self, event): 
        pass
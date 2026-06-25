#Arquivo para gerir as dependências para figuras

from abc import ABC, abstractmethod

class Figuras(ABC):
    """Classe abstrata para as figuras"""

    @abstractmethod
    def draw(self): #O que o botão faz após clicado
        pass


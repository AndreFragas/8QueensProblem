import numpy as np

class ChessTable :
    def __init__(self, quantidadeRainhas):
        self.linha = quantidadeRainhas
        self.coluna = quantidadeRainhas
        self.tabuleiro = np.zeros((quantidadeRainhas, quantidadeRainhas))
        
    def get_property(self, property_name):
        return getattr(self, property_name)
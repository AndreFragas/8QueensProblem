import numpy as np

class ChessTable :
    def __init__(self, quantidadeRainhas):
        self.linha = quantidadeRainhas
        self.coluna = quantidadeRainhas
        self.tabuleiro = np.zeros((quantidadeRainhas, quantidadeRainhas))
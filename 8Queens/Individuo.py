class Individuo :
    def __init__(self, geracao, listaPosicoes):
        self.geracao = geracao
        self.listaPosicoes = listaPosicoes
        self.fitness = 0
    
    def get_property(self, property_name):
        return getattr(self, property_name)
    
    def set_Fitness(self, value: int):
        self.fitness = value
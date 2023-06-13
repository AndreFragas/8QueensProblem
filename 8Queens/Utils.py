from Individuo import Individuo
import random

def gerarIndividuosIniciais(quantidadeIndividuos, quantidadeRainhas):
    indice = 0
    listaIndividuos : Individuo = []
    
    while(indice < quantidadeIndividuos):
        individuo = Individuo(1, randomizerPosicaoRainhas(quantidadeRainhas))
        listaIndividuos.append(individuo)
        indice = indice + 1
     
    return listaIndividuos

def randomizerPosicaoRainhas(quantidadeRainhas):
    listaPosicoes = random.sample(range(0, quantidadeRainhas), quantidadeRainhas)
    
    return listaPosicoes

def getFitness(tableChess, individuo : Individuo):
    fitness = 0
    table = tableChess
    
    for index, rainha in enumerate(individuo.listaPosicoes):
        table[rainha][index] = 1
        
    for linha in table:
        for coluna in linha:
            print(coluna, end=' ')
        print()
    
        
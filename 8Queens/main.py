from Utils import *
from typing import List
from ChessTable import ChessTable

def main():
    print("Que comecem os jogos:" )
    quantidadeRainhas = int(input("Digite um número para a quantidade de rainhas e tamanho do tabuleiro: "))
    
    newGeneration : List[Individuo] = gerarIndividuosIniciais(8, quantidadeRainhas)
    chessTable = ChessTable(quantidadeRainhas)
    
    for individuo in newGeneration:
        individuo.set_Fitness(getFitness(chessTable.tabuleiro, individuo))
        chess = ChessTable(quantidadeRainhas)
        # for index, rainha in enumerate(individuo.listaPosicoes):
        #     chess.tabuleiro[rainha][index] = 1
        # printChessTable(chess.tabuleiro)
        # print(individuo.listaPosicoes)
        # print(individuo.fitness)
        
    # while (verifyWinner(newGeneration, quantidadeRainhas) == False):
    
    #     melhoresIndividuos : List[Individuo] = getMelhoresIndividuos(newGeneration)
    #     newGeneration = gerarIndividuosPorCrossover(melhoresIndividuos[0], melhoresIndividuos[1])
    #     newGeneration = mutation(newGeneration)
    
    # print("Acabouuuuuuuuuuuuuu")
    
main()
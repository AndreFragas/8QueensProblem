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

    for i in newGeneration:
      i.set_Fitness(getFitness(chessTable.tabuleiro, i))

    while (verifyWinner(newGeneration, quantidadeRainhas) == False):
        melhor_1, melhor_2 = getMelhoresIndividuos(newGeneration)
        newGeneration = gerarIndividuosPorCrossover(melhor_1, melhor_2, 8)
        for i in newGeneration:
          i.set_Fitness(getFitness(chessTable.tabuleiro, i))
        newGeneration = mutation(newGeneration)

    print("Acabouuuuuuuuuuuuuu")

main()
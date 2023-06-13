from Utils import *
from typing import List
from ChessTable import ChessTable

def main():
    print("Que comecem os jogos:" )
    quantidadeRainhas = int(input("Digite um número para a quantidade de rainhas e tamanho do tabuleiro: "))
    
    listaIndividuosIniciais : List[Individuo] = gerarIndividuosIniciais(8, quantidadeRainhas)
    chessTable = ChessTable(quantidadeRainhas)
    
    for individuo in listaIndividuosIniciais:
        getFitness(chessTable.tabuleiro, individuo)

    # for linha in chessTable.tabuleiro:
    #     for coluna in linha:
    #         print(coluna, end=' ')
    #     print()
    
    # for individuo in listaIndividuosIniciais:
    #    for i in individuo.listaPosicoes:
    #        print(i)
    #    print("---")
    
main()
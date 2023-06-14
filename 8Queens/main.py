from Utils import *
from typing import List
from ChessTable import ChessTable

def main():
    print("Que comecem os jogos:" )
    quantidadeRainhas = int(input("Digite um número para a quantidade de rainhas e tamanho do tabuleiro: "))
    
    listaIndividuosIniciais : List[Individuo] = gerarIndividuosIniciais(2, quantidadeRainhas)
    chessTable = ChessTable(quantidadeRainhas)
    
    for index ,individuo in listaIndividuosIniciais:
        auxiliar = listaIndividuosIniciais[index]
        auxiliar.set_Fitness(getFitness(chessTable.tabuleiro, individuo))
        listaIndividuosIniciais[index] = auxiliar
        
    for individuo in listaIndividuosIniciais:
        table = copy.deepcopy(chessTable.tabuleiro)
        
        for index, rainha in enumerate(individuo.listaPosicoes):
            table[rainha][index] = 1
            
        printChessTable(table)
    
main()
from typing import List
from Individuo import Individuo
from ChessTable import ChessTable
import random
import copy

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
    table = copy.deepcopy(tableChess)

    for index, rainha in enumerate(individuo.listaPosicoes):
        table[rainha][index] = 1

    for index ,rainha in enumerate(individuo.listaPosicoes):
        fitness += getNumberOfConflitsInRow(table, rainha, index) + getNumberOfConflitsInCollumn(table, rainha, index) + getNumberOfConflitsInDiagonally(table, rainha, index)

    return fitness

def getNumberOfConflitsInRow(table, row, column):
    conflits = 0
    for linha in range(len(table)):
        for coluna in range(len(table[linha])):
            if (linha == row):
                if (table[linha][coluna] == 1 and coluna != column):
                    conflits += 1

    return conflits

def getNumberOfConflitsInCollumn(table, row, collumn):
    conflits = 0
    for linha in range(len(table)):
        for coluna in range(len(table[linha])):
            if (coluna == collumn):
                if (table[linha][coluna] == 1 and linha != row):
                    conflits += 1

    return conflits

def getNumberOfConflitsInDiagonally(table, row, collumn):
    conflits = 0
    size = len(table)

    r = row - 1
    c = collumn - 1
    while r >= 0 and c >= 0:
        if table[r][c] == 1:
            conflits += 1
        r -= 1
        c -= 1

    r = row + 1
    c = collumn + 1
    while r < size and c < size:
        if table[r][c] == 1:
            conflits += 1
        r += 1
        c += 1

    r = row - 1
    c = collumn + 1
    while r >= 0 and c < size:
        if table[r][c] == 1:
            conflits += 1
        r -= 1
        c += 1

    r = row + 1
    c = collumn - 1
    while r < size and c >= 0:
        if table[r][c] == 1:
            conflits += 1
        r += 1
        c -= 1

    return conflits

def printChessTable(chessTable):
    for linha in chessTable:
        for coluna in linha:
            print(coluna, end=' ')
        print()

def getMelhoresIndividuos(listaIndividuos: List[Individuo]):
    best1 = listaIndividuos[0]
    best2 = listaIndividuos[1]

    if(best1.listaPosicoes == best2.listaPosicoes):
      best2 = listaIndividuos[2]

    for individuo in listaIndividuos[2:]:
        if(best1.fitness < best2.fitness):
          if(best2.fitness > individuo.fitness):
            best2 = individuo
        else:
          if(best1.fitness > individuo.fitness):
            best1 = individuo

    if(best1.listaPosicoes == best2.listaPosicoes):
      newIndividuo = Individuo(best1.geracao, randomizerPosicaoRainhas(len(best1.listaPosicoes) ))
      return best1, newIndividuo

    return best1, best2

def gerarIndividuosPorCrossover(pai, mae, gen):
    listaIndividuos : List[Individuo] = []

    for i in range(gen):
        corte = random.randint(0, len(pai.listaPosicoes))
        paiList = pai.listaPosicoes[0: corte]
        maeList = mae.listaPosicoes[corte: ]
        lista = []
        for p in paiList:
            lista.append(p)
        for m in maeList:
            lista.append(m)
        newIndividuo = Individuo(pai.geracao + 1, lista)
        listaIndividuos.append(newIndividuo)
    return listaIndividuos

def mutation(generation, chance = 20):
    listaIndividuos : List[Individuo] = []
    for individuo in generation:
        chance = random.randint(1, chance)

        if (chance == 1):
            rainha1 = random.randint(0, len(individuo.listaPosicoes) - 1)
            rainha2 = random.randint(0, len(individuo.listaPosicoes) - 1)
            auxiliar = individuo.listaPosicoes[rainha1]
            individuo.listaPosicoes[rainha1] = individuo.listaPosicoes[rainha2]
            individuo.listaPosicoes[rainha2] = auxiliar

        listaIndividuos.append(individuo)

    return listaIndividuos

def verifyWinner(listaIndividuos, quantidadeRainhas):
    for individuo in listaIndividuos:
        if (individuo.fitness == 0):
            chessTable = ChessTable(quantidadeRainhas)

            for index, rainha in enumerate(individuo.listaPosicoes):
                chessTable.tabuleiro[rainha][index] = 1

            printChessTable(chessTable.tabuleiro)
            print(individuo.listaPosicoes)
            print(individuo.geracao)
            return True

    return False
        
        
        
    
        
        
    
    
    
    
        
    
        
from Individuo import Individuo
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
        
    printChessTable(table)
        
    for index ,rainha in enumerate(individuo.listaPosicoes):
        # print("Linha ",index,": ",getNumberOfConflitsInRow(table, rainha, index))
        # print("Coluna ",index,": ",getNumberOfConflitsInCollumn(table, rainha, index))
        # print("Diagonal",index,": ",getNumberOfConflitsInDiagonally(table, rainha, index))
        fitness = getNumberOfConflitsInRow(table, rainha, index) + getNumberOfConflitsInCollumn(table, rainha, index) + getNumberOfConflitsInDiagonally(table, rainha, index)
        
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
    
        
    
        
    
        
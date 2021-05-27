# -*- coding: utf-8 -*-

#Lista 10

#2) Uma matriz quadrada inteira é chamada de "quadrado mágico" se a soma dos elementos de cada
#linha, a soma dos elementos de cada coluna e a soma dos elementos das diagonais principal e
#secundária são todos iguais. Exemplo: As matrizes abaixo representam quadrados mágicos:
# | 8 0 7 | | 4 9 2 |
# | 4 5 6 | | 3 5 7 |
# | 3 10 2 | | 8 1 6 |
#Escreva um programa que verifica se uma matriz de 3 linhas e 3 colunas representa um quadrado mágico.

import numpy as np

def verifica_matriz(A):
    linha = np.zeros([3])
    coluna = np.zeros([3])
    diag_princp = 0
    diag_sec =  A[0,2] +  A[1,1] +  A[2,0]
    for i in range(0,3):       
        for j in range(0,3):   
            linha[i] = linha[i] + A[i,j]
            coluna[j] = coluna[j] + A[i,j]
            if i == j:
                diag_princp = diag_princp + A[i,j]
    
    if linha[0] == linha[1] == linha[2] == coluna[0] == coluna[1] == coluna[2] == diag_princp == diag_sec:
        print('A matriz representa um quadrado mágico!')
        
A = np.array([[4, 9, 2], [3, 5, 7], [8, 1, 6]])
verifica_matriz(A)
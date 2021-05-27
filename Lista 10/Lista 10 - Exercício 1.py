# -*- coding: utf-8 -*-

#Lista 10

#1) Faça um programa que preencha uma matriz 4x5 com números inteiros randômicos. 
#Mostre essa matriz na tela e informe a posição e o valor do maior e do menor número encontrado.

from random import randint
import numpy as np

matriz = np.zeros([4,5]) #cria matriz nula
maximo = 0
minimo = 100

#preenche a matriz
for i in range(0,4):
    for j in range(0,5):
        n = randint(0,100)
        matriz[i,j] = n
        if matriz[i,j] > maximo:
            maximo = matriz[i,j]
            pos_max = [i,j]
        if matriz[i,j] < minimo:
            minimo = matriz[i,j]
            pos_min = [i,j]
        
print(matriz)
print('Máximo valor:', maximo, 'encontrado na linha',pos_max[0]+1, 'e coluna', pos_max[1]+1)
print('Mínimo valor:', minimo, 'encontrado na linha',pos_min[0]+1, 'e coluna', pos_min[1]+1)


# -*- coding: utf-8 -*-

#Lista 10

#4) Ler a diagonal principal de uma matriz de 4x4 e preencher as células acima da diagonal com 1 e as
#abaixo com 2.

import numpy as np

A = np.random.randint(10,size=[4,4]) #matriz aleatória
print('Matriz A antes:\n',A)

for i in range(0,4):
    for j in range(0,4):
        if i > j:
            A[i,j] = 2
        elif i < j:
            A[i,j] = 1
print('\nMatriz A depois:\n',A,)
# -*- coding: utf-8 -*-

#Lista 10

#7) Usando uma matriz 3x3 crie um jogo da velha. O jogador número 1 usa o X e o jogador 2 é representado pelo O.
#O programa deve sortear quem inicia o jogo. O jogador deve indicar a linha e a coluna que quer jogar. 
#Se a casa já estiver ocupada o jogador deve selecionar outra casa. 
#Ganha quem fizer uma sequência de símbolos iguais em uma linha, coluna ou diagonal.

import numpy as np
from random import randint

def verificar_ganhou(A):
    for i in range(0,3): #checar as linhas do tabuleiro
        soma = A[i,0] + A[i,1] + A[i,2]
        if soma == 3 or soma == -3:
            return 1

    for i in range(0,3): #checar as colunas do tabuleiro
        soma = A[0,i] + A[1,i] + A[2,i]
        if soma == 3 or soma == -3:
            return 1

    diag1 = A[0,0] + A[1,1] + A[2,2]  #checar as diaonais
    diag2 = A[0,2] + A[1,1] + A[2,0]
    if diag1 == 3 or diag1 == -3 or diag2 == 3 or diag2 ==-3:
        return 1

    return 0


A = np.empty([3,3], dtype = str)
j = np.zeros([3,3])

jogador = randint(1,2)

print('Quem começa é jogador', jogador)
parar = 0

while parar == 0:
    print('\n',A[0,0],'|', A[0,1] ,'|', A[0,2], '\n __________ \n',A[1,0],'|', A[1,1] ,'|', A[1,2],' \n __________ \n', A[2,0],'|', A[2,1] ,'|', A[2,2],)    
    linha = int(input('Indica a linha que quer jogar: '))
    coluna = int(input('Indica a coluna que quer jogar: '))
    if A[linha-1,coluna-1]:
        print('Espaço ocupado, escolha outra casa!')
        linha = int(input('Indica a linha que quer jogar: '))
        coluna = int(input('Indica a coluna que quer jogar: '))
    if jogador == 1:
        A[linha-1,coluna-1] = 'X'
        j[linha-1,coluna-1] = 1
        jogador = 2
    else:
        A[linha-1,coluna-1] = 'O'
        j[linha-1,coluna-1] = -1
        jogador = 1
        
    parar = verificar_ganhou(j)
    
    if parar == 1:
        print('\n',A[0,0],'|', A[0,1] ,'|', A[0,2], '\n __________ \n',A[1,0],'|', A[1,1] ,'|', A[1,2],' \n __________ \n', A[2,0],'|', A[2,1] ,'|', A[2,2],)    
        if jogador == 1:
            print('Jogador 2 ganhou!')
        if jogador == 2:
            print('Jogador 1 ganhou!')
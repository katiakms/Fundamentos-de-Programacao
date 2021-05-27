# -*- coding: utf-8 -*-

#Lista 10

#6) Leia uma matriz 5x10 que se refere respostas de 10 questões de múltipla escolha, referentes a 5 alunos. 
#Leia também um vetor de 10 posições contendo o gabarito de respostas que podem ser a, b, c ou d. 
#Seu programa deverá comparar as respostas de cada candidato com o gabarito e emitir um
#vetor denominado resultado, contendo a pontuação correspondente a cada aluno.

import numpy as np

A = np.empty([5,10], dtype = str)
gabarito = np.empty([10], dtype = str)
correcao = np.zeros([5,10])

for i in range(0,5):
    for j in range(0,10):
        A[i,j] = input('Aluno {} digite a respota da questão {}: '.format(i+1,j+1))
        

for i in range(0,10):
    gabarito[i] = input('Digite o gabarito da questão {}: '.format(i+1))
    
for i in range(0,5):
    for j in range(0,10):
        if A[i,j] == gabarito[j]:
            correcao[i,j] = 1
            
result = [sum(correcao[0,:]), sum(correcao[1,:]), sum(correcao[2,:]), sum(correcao[3,:]), sum(correcao[4,:])]

print('Resultado: \nAluno 1 nota',result[0],'\nAluno 2 nota',result[1],'\nAluno 3 nota',result[2])
print('Aluno 4 nota',result[3],'\nAluno 5 nota',result[4])
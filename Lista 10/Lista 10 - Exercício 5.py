# -*- coding: utf-8 -*-
#Lista 10

#5)Fazer um programa que armazene os valores arrecadados por uma loja em cada um dos três turnos
#(manhã, tarde, noite) durante uma semana (segunda até sábado). Ao final da semana indicar:
#a) Exibir todas as vendas de cada dia da semana (na forma de tabela)
#b) Qual o turno com maior venda
#c) Qual o turno com menor venda
#d) Qual o dia da semana com maior venda
#e) Qual o dia da semana com menor venda
#f) Qual o total arrecadado durante a semana
#Resolver o problema utilizando uma matriz com um tamanho definido por você.

import numpy as np
import pandas as pd

A = np.zeros([6,3]) #linhas = dia da semana, coluna = turno
turnos = ['Manhã', 'Tarde', 'Noite']
dia_semana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']

menor = 0
total = 0

for i in range(0,len(dia_semana)):
    for j in range(0,len(turnos)):
        print('Dia:', dia_semana[i],'Turno:', turnos[j])
        a = float(input('Digite o valor arrecadado: '))
        A[i,j] = a
        total = total+a
        
venda_turnos = [sum(A[:,0]),sum(A[:,1]),sum(A[:,2])] #vetor com o total de vendas de cada turno
venda_dia = [sum(A[0,:]),sum(A[1,:]),sum(A[2,:]),sum(A[3,:]),sum(A[4,:]),sum(A[5,:]),] #vetor com o total de vendas de cada dia

maior_dia = venda_dia.index(max(venda_dia)) #acha a posição no vetor da maior venda entre os turnos
maior_turno = venda_turnos.index(max(venda_turnos)) #acha a posição no vetor da maior venda entre os dias

menor_dia = venda_dia.index(min(venda_dia)) #acha a posição no vetor da menor venda entre os turnos
menor_turno = venda_turnos.index(min(venda_turnos)) #acha a posição no vetor da menor venda entre os dias

df = pd.DataFrame(A, dia_semana, turnos) #transforma matriz A em um dataframe (tabela)
print(df)
print('Turno com maior venda:',turnos[maior_turno])
print('Dia da semana com maior venda:',dia_semana[maior_dia])
print('Turno com menor venda:',turnos[menor_turno])
print('Dia da semana com menor venda:',dia_semana[menor_dia])
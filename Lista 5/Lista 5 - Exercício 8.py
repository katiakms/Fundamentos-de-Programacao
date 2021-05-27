# -*- coding: utf-8 -*-

#Lista 5

#8) Faça um programa que leia a nota do Grau A e do Grau B do aluno e calcule a média final conforme
#as regras da Unisinos. Imprima a média final na tela e diga se o aluno passou por média ou se
#ficou em recuperação (grau C). Se o aluno ficou em recuperação, pergunte se ele quer substituir
#o Grau A ou o Grau B (ele deve digitar ‘a’ ou ‘b’). Leia a nota do Grau C, recalcule a média de
#acordo com o grau substituído e imprima na tela o resultado, informando se ele foi aprovado ou
#reprovado.

grau_A = input('Digite a nota do grau A: ')
grau_B = input('Digite a nota do grau B: ')

media_final = 1/3*float(grau_A) + 2/3 * float(grau_B)

if (media_final < 7):
    print('Você ficou em recuperação')
    substituir = input('Você quer substituir a nota do grau A (digite A) ou grau B (digite B)? ')
    grau_C = input('Digite a nota do grau C: ')
    if (substituir == 'A'):
        media_final2 =  1/3*float(grau_C) + 2/3 * float(grau_B)
    elif (substituir == 'B'):
        media_final2 = 1/3*float(grau_A) + 2/3 * float(grau_C)
    
    if (media_final2 > 7):
        print(f'Você foi aprovado! Nota final: {media_final2:.1f}')
    else:
        print(f'Você reprovou. Nota final: {media_final2:.1f} ')
else:
    print(f'Você foi aprovado! Nota final: {media_final:.1f} ')
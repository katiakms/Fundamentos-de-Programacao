# -*- coding: utf-8 -*-

#Lista 5

#5) Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule
#seu peso ideal, utilizando as seguintes fórmulas:
#- para homens: (72.7 * h) - 58;
#- para mulheres: (62.1 * h) - 44.7.

altura = input('Entre a altura da pessoa em metros: ')
sexo = input('Entre o sexo da pessoa (H - homem, M - mulher): ')

if (sexo == 'H'):
    peso_ideal = (72.7 * float(altura)) - 58
else:
    peso_ideal = (62.1 * float(altura)) - 44.7
    
print('O peso ideal é: ', peso_ideal, 'kg')
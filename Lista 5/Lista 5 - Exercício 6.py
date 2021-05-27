# -*- coding: utf-8 -*-

#Lista 5

#6) Crie um programa para informar quais e quantas notas são necessárias para entregar o mínimo
#de cédulas para um determinado valor informado pelo usuário considerando notas de R$ 100,
#R$ 50, R$ 20, R$ 10 e R$ 5 e R$ 1. Seu programa deve mostrar apenas as notas utilizadas. Por
#exemplo, ao solicitar R$18, o programa deve informar apenas a seguinte informação (note que
#não foram exibidas informações sobre as demais cédulas):
#1 nota(s) de R$ 10.
#1 nota(s) de R$ 5.
#3 nota(s) de R$ 1.

valor = input('Entre com o valor informado: ')

temp = float(valor)

div_100 = int(float(valor)/100)
temp = temp - div_100*100

div_50 = int(temp/50)
temp = temp - div_50*50

div_20 = int(temp/20)
temp = temp - div_20*20

div_10 = int(temp/10)
temp = temp - div_10*10

div_5 = int(temp/5)
temp = temp - div_5*5

div_1 = int(temp/1)
temp = temp - div_1*1

if (div_100 != 0):
    print(div_100, 'nota(s) de R$ 100')
if (div_50 != 0):
    print(div_50, 'nota(s) de R$ 50')
if (div_20 != 0):
    print(div_20, 'nota(s) de R$ 20')
if (div_10 != 0):
    print(div_10, 'nota(s) de R$ 10')
if (div_5 != 0):
    print(div_5, 'nota(s) de R$ 5')
if (div_1 != 0):
    print(div_1, 'nota(s) de R$ 1')
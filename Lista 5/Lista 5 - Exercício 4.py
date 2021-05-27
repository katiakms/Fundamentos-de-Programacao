# -*- coding: utf-8 -*-
#Lista 5

#4)Um comerciante comprou um produto e quer vendê-lo com lucros diferentes dependendo do valor da compra. 
#Ele quer um lucro de 45% se o valor da compra for menor que R$ 20,00, 35% se o preço for de até 50 reais e
#lucro de 25% se valor for maior. Entrar com o valor do produto e imprimir na tela o valor de venda.

valor = input('Entre o valor do produto: ')

if (float(valor) < 20):
    lucro = 45/100
elif (float(valor) < 50):
    lucro = 35/100
else:
    lucro = 25/100

valor_final = float(valor) + float(valor)*lucro
    
print('O valor de venda é: ', valor_final)
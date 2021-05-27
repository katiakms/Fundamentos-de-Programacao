# -*- coding: utf-8 -*-

#Lista 5

#10) Elabore um algoritmo que calcule o que deve ser pago por um produto, considerando o preço
#normal de etiqueta e a escolha da condição de pagamento. Utilize os códigos da tabela a seguir
#para ler qual a condição de pagamento escolhida e efetuar o cálculo adequado.
#1 - À vista em dinheiro, recebe 15% de desconto
#2 - À vista no cartão de crédito, recebe 10% de desconto
#3 - Em duas vezes, preço normal de etiqueta sem juros
#4 - Em três vezes, preço normal de etiqueta mais juros de 10%

valor = input('Digite o valor do produto: ')
print('Os métodos de pagamento são: \n1 - À vista em dinheiro, recebe 15% de desconto'
      '\n2 - À vista no cartão de crédito, recebe 10% de desconto'
     '\n3 - Em duas vezes, preço normal de etiqueta sem juros'
      '\n4 - Em três vezes, preço normal de etiqueta mais juros de 10%')

metodo = input('Digite o método de pagamento: ')

if (int(metodo) == 1):
    valor_final = float(valor) - float(valor)*15/100
elif (int(metodo) == 2):
    valor_final = float(valor) - float(valor)*10/100
elif (int(metodo) == 3):
    valor_final = float(valor)
elif (int(metodo) == 4):
    valor_final = float(valor) + float(valor)*10/100
    
print('O valor final é:', valor_final)


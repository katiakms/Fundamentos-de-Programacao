# -*- coding: utf-8 -*-

#Lista 5

#3) Implementar um programa que calcula o desconto previdenciário de um funcionário.
#A classe deve, dado um salário retornar o valor do desconto proporcional ao mesmo.
#Entretanto, o cálculo de desconto segue a regra: o desconto deve 11% do valor do salário, entretanto, o valor máximo
#de desconto é 318,20. Sendo assim, ou o método retorna 11% sobre o salário ou 318,20

salario = input('Entre o valor do salário: ')
desconto = 11/100

desconto_do_salario = float(salario)*desconto
valor_maximo = 318.20

if (desconto_do_salario > valor_maximo):
    print('O salário é:', salario)
else:
    salario_desconto = float(salario) - desconto_do_salario
    print('O salário é:', salario_desconto)
# -*- coding: utf-8 -*-
#Lista 5

#9) Criar um programa para identificar o valor a ser pago por um plano de saúde dada a idade do
#conveniado considerando que todos pagam R$ 300 e mais um adicional (se tiver dependentes)
#conforme a seguinte tabela:
#a) crianças com menos de 10 anos pagam R$100;
#b) dependentes com idade entre 10 e 30 anos pagam R$220;
#c) dependentes com idade entre 31 e 60 anos pagam R$ 395; e
#d) dependentes com mais de 60 anos pagam R$ 480.

dependente = input('Você tem dependentes? (s = sim, n = não) ')

if (dependente == 's'):
    dep1 = input('Digite quantos dependentes com menos de 10 anos: ')
    dep2 = input('Digite quantos dependentes com idade entre 10 e 30 anos: ')
    dep3 = input('Digite quantos dependentes com idade entre 31 e 60 anos: ')
    dep4 = input('Digite quantos dependentes com mais de 60 anos: ')
    valor = 300 + int(dep1)*100 + int(dep2)*220 + int(dep3)*395 + int(dep4)*480
else:
    valor = 300
    
print('Valor a ser pago:', valor)
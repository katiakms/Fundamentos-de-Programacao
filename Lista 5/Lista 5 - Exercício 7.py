# -*- coding: utf-8 -*-

#Lista 5

#7)  A confederação brasileira de natação irá promover eliminatórias para o próximo mundial. Fazer
#um algoritmo que receba a idade de um nadador e imprima a sua categoria segundo a tabela a seguir:

idade = input('Entre a idade do nadador: ')

if (5 <= int(idade) <= 7):
    print('Categoria Infantil A')
elif (8 <= int(idade) <= 10):
    print('Categoria Infantil B')
elif (11 <= int(idade) <= 13):
    print('Categoria Juvenil A')
elif (14 <= int(idade) <= 17):
    print('Categoria Juvenil B')
elif (int(idade) >= 18):
    print('Categoria Sênior')
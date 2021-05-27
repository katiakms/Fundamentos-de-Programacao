#Prova 1 - Cíntia

#2) Uma empresa de logística cobra o frete de acordo com o volume da embalagem, o peso da encomenda e a 
#distância percorrida entre origem e destino. Faça um programa que solicita ao usuário a base, altura e 
#profundidade de um pacote (cm), o peso total (kg) e a distância percorrida (km). 
#Calcule e mostre na tela o volume da embalagem (cm3) e o valor do frete (R$). 
#O valor do frete é dado pela equação volume * peso * distância / 200000.

#O programa deve rodar enquanto o usuário não dizer que quer sair.
#Exemplo:

#Informe a base:
#Informe a altura:
#Informe a profundidade:
#Informe o peso:
#Informe a distância percorrida:

#O volume da embalagem é de XX cm³
#O valor do frete da encomenda é de R$ XX

#Deseja calcular outra encomenda? (S/N):
    
while True:

    base = float(input('Informe a base em cm: '))
    altura = float(input('Informe a altura em cm: '))
    profundidade = float(input('Informe a profundidade em cm: '))
    peso = float(input('Informe o peso total em kg: '))
    distancia = float(input('Informe a distância percorrida em km: '))

    volume = base*altura*profundidade #calcula o volume em cm³
    frete = (volume*peso*distancia)/200000 #calcula o frete

    print('\nO volume da embalagem é de', volume,'cm³')
    print('O valor do frete da encomenda é de R$', frete)

    outra_encomenda = input('Deseja calcular outra encomenda? (S/N): ')

    if outra_encomenda == 'N':
        break #se a resposta for não, termina o programa
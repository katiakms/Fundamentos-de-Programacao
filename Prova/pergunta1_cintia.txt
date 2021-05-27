#Prova 1 - Cíntia

#1)Foi feita uma pesquisa entre os habitantes de uma região e coletados os dados de altura, a idade e sexo das pessoas.
#Faça um programa que leia 50 dados diferentes e, ao final, informe: 

#A.a maior e a menor altura encontradas 
#B.a média de altura das mulheres 
#C.a média de idade da população 
#D.o percentual de crianças até 12 anos na população 
#E.a altura e a idade do homem mais baixo 

cont = 0 
total_pessoas = 4 #número de pessoas entrevistadas
criancas = 0 #contador numero de crianças
mulheres = 0 #contador numero de mulheres
homens = 0 #contador numero de homens

altura_vetor = [] #vetor para guardar todas as alturas
altura_mulheres = [] #vetor para guardar as alturas das mulheres
altura_homens = [] #vetor para guardar as alturas dos homens

idade_vetor = [] #vetor para guardar todas as idades
idade_homens = [] #vetor para guardar idade dos homens 


while cont < total_pessoas:
    altura = float(input('Digite a altura em cm do entrevistado: '))
    idade = int(input('Digite a idade do entrevistado: '))
    sexo = input('Digite o sexo do entrevistado (F = feminino, M = masculino): ')
    
    altura_vetor.append(altura) #vetor com todas as alturas
    idade_vetor.append(idade) #vetor com todas as idades  
    
    if sexo == 'F':
        altura_mulheres.append(altura) #se for mulher, salva altura no vetor
        mulheres = mulheres+1 #conta numero de mulheres
    else:
        altura_homens.append(altura) #se for homem, salva altura
        idade_homens.append(idade) #se for homem, salva idade
        homens = homens + 1 #conta numero de homens
    
    if idade < 12:
        criancas = criancas + 1 #contagem de crianças até 12 anos 
    
    cont = cont+1

maior_altura = max(altura_vetor) #altura máxima
menor_altura = min(altura_vetor) #altura mínima

if mulheres != 0: #se o numero de mulheres não for zero, calcula a media das alturas
    media_altura_mulheres = sum(altura_mulheres)/mulheres
else:
    media_altura_mulheres = 0
    
media_idade = sum(idade_vetor)/total_pessoas

if criancas != 0: #se o numero de crianças não for zero, calcula a porcentagem de crianças na população
    percentual_criancas = criancas/total_pessoas * 100
else:
    percentual_criancas = 0

if homens != 0: #se o numero de homens não for zero, acha a idade e altura do homem mais baixo
    homem_baixo = min(altura_homens)
    index_homem_baixo = altura_homens.index(homem_baixo)
    idade_homem_baixo = idade_homens[index_homem_baixo]
else:
    homem_baixo = 0
    idade_homem_baixo = 0

    
print('\nA maior altura encontrada:', maior_altura, 'cm')
print('A menor altura encontrada:', menor_altura, 'cm')
print('A média de altura das mulheres:', media_altura_mulheres, 'cm')
print('A média de idade da população:', media_idade)
print('O percentual de crianças até 12 anos na população:', percentual_criancas, '%')
print('A altura e a idade do homem mais baixo:', homem_baixo, 'cm,', idade_homem_baixo, 'anos')
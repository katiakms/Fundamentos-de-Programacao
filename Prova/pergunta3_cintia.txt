#Prova 1 - Cíntia

#3)Crie uma função que receba por parâmetro três valores inteiros positivos: início, fim e num.
#A função deve imprimir na tela todos os números pares menores do que o num e todos os ímpares
#maiores do que num do início ao fim do intervalo. Num não deve ser impresso.

#Exemplo:

#Se for informado: paresImpares(10, 30, 20), 
#o programa deve imprimir na tela: 10, 12, 14, 16, 18, 21, 23, 25, 27, 29.

def paresImpares(inicio, fim, num):
    
    cont = inicio #contador que vai ser igual o numero inicial do intervalo
    
    while inicio <= cont < num: #enquanto o contador estiver entre o valor inicial e num, está no loop
        if (cont%2 == 0): #se o número for par, imprime na tela
            print(cont)
        cont = cont+1 #soma um ao contador
        
    while num <= cont <= fim: #enquanto o contador estiver entre o num e o valor final, está no loop
        if (cont%2 != 0): #se o número for ímpar, imprime na tela
            print(cont)
        cont = cont+1 #soma um ao contador
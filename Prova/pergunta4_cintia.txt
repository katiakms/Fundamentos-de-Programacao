# Prova 1 - Cíntia

#4) Crie uma função que receba dois números inteiros por parâmetro, n1 e n2. intervalo(n1,n2)
#A função deve imprimir na tela uma sequência de 5 números fracionários partindo de n1 até atingir n2, 
#com intervalos regulares.

#A sequência pode ser tanto crescente quanto decrescente. 

#Exemplos:
#intervalo(3, 12) Sequência impressa na tela: 3,00 5,25 7,50 9,75 12,00
#intervalo(35, 18) Sequência impressa na tela: 35,00 30,75 26,50 22,25 18,00

def intervalo(n1, n2):
    quant_num = 5 #quantidade de numeros no intervalo
    num_final = n1 #inicial a variável igual ao primeiro numero do intervalo
    
    print(n1) #imprime o primeiro valor da sequência
    interv = (n2 - n1)/(quant_num-1) #calcula o intervalo igual entre os números
    
    for i in range(1,quant_num): #loop de 1 até 5 para imprimir os outros números na tela
        num_final = num_final+interv #soma o num_final com ele mesmo mais o intervalo
        print(num_final) #imprime o próximo valor da sequência
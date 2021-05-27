def gera_relatorio(peso_pacotes,valor_pacotes,quantidade_pacotes,peso_parada,peso_excedente,valor_excedente):
    #verifica que os vetores não estão vazios, se estiverem da o valor de zero
    if peso_pacotes == []:
        peso_pacotes.append(0)
    if quantidade_pacotes == []:
        quantidade_pacotes.append(0)
    if peso_parada == []:
        peso_parada.append(0)
    if peso_excedente == []:
        peso_excedente.append(0)
    if valor_excedente == []:
        valor_excedente.append(0)
    print('Menor peso de pacote individual transportado durante todo o dia:', min(peso_pacotes))
    print('Maior peso de pacote individual transportado durante todo o dia:', max(peso_pacotes))
    print('Menor quantidade de pacotes embarcados em uma parada:', min(quantidade_pacotes))
    print('Maior quantidade de pacotes embarcados em uma parada:', max(quantidade_pacotes))
    print('Menor quantidade total de peso no caminhão ao encerrar parada:', min(peso_parada))
    print('Maior quantidade total de peso no caminhão ao encerrar parada:', max(peso_parada))
    print('Maior peso excedente durante todo o dia:', max(peso_excedente))
    print('Maior valor excedente durante todo o dia:', max(valor_excedente))
    
def parada(peso_max,peso_pacotes,quantidade_pacotes,peso_parada,peso_excedente,valor_excedente):
    #inicia variáveis de contagem como zero
    pacote = 0
    peso_na_parada = 0
    peso_exc = 0
    while True:
        op2 = input('Digite a opção desejada: ') #pede para o usuário escolher a opção 
        if op2 == 'a':
            peso = float(input('Digite o peso do pacote (entre 1 e 99 kg): ')) #pede para o usuário o peso da mercadoria
            
            if (sum(peso_pacotes)+peso) > peso_max:
                print('Peso máximo atingido! Pacote não embarcado!')
            else:
                preco = float(input('Digite o valor da mercadoria: ')) #pede para o usuário o preço da mercadoria                
                custo_total = custo*peso #calcula o custo de transporte
                print('O custo de transporte é R$', custo_total)

                if (sum(peso_pacotes)+peso) > 10*capacidade_max: #seguradora cobre apenas o valor em peso de 10 vezes o volume de carga máxima do caminhão
                    custo_seguro = 0.8 #R$ 0.80 a cada quilo excendente
                    excedente = sum(peso_pacotes) + peso - 10*capacidade_max #excedente em quilos
                    seguro_total = custo_seguro*excedente #calcula o valor adicional do seguro
                    print('Será necessário um valor adicional referente ao seguro de R$', seguro_total)
                    quer_seguro = input('Você aceita pegar o valor adicional? (S - sim, N - não) ')
                    if quer_seguro == 'S': # se o usuário aceitar o seguro, salva o peso, valor e conta o pacote e seu peso
                        peso_pacotes.append(peso)
                        valor_pacotes.append(preco)
                        valor_excedente.append(seguro_total)
                        pacote = pacote+1
                        peso_na_parada = peso_na_parada + peso
                        peso_exc = peso_exc + excedente                   
                        print('Pacote embarcado no caminhão!')
                    elif quer_seguro == 'N': #se o usuário não aceitar o seguro não faz nada 
                        print('Pacote não embarcado no caminhão!')
                else: #se não for necessário valor excedente de seguro, salva os valores
                    peso_pacotes.append(peso) 
                    valor_pacotes.append(preco)
                    pacote = pacote+1
                    peso_na_parada = peso_na_parada + peso
                    print('Pacote inserido!')
        elif op2 == 'b':
            if peso_pacotes == []: #se o vetor estiver vazio, não há nada para descarregar
                print('Não existe nada para ser descarregado!')
            else:
                ultimo_carregado = peso_pacotes[-1] #pega o peso do ultimo valor da lista 
                valor_ultimo_carregado = valor_pacotes[-1] #pega o valor do ultimo valor da lista 
                print('O último carregado possui',ultimo_carregado,'kg')
                quer_retirar = input('Você deseja retirar o pacote? (S - sim, N - não) ')
                if quer_retirar == 'S':
                    peso_pacotes.remove(ultimo_carregado) #remove o peso do pacote da lista, descarregando do caminhão
                    valor_pacotes.remove(valor_ultimo_carregado) #remove o valor do pacote da lista, descarregando do caminhão
                    print('Pacote retirado!')
                elif quer_retirar == 'N':
                    print('Pacote não retirado!')
        elif op2 == 'c':
            quantidade_pacotes.append(pacote) #quando terminar a parada, salva as quantidade de pacotes carregadas na parada
            peso_parada.append(peso_na_parada) #quando terminar a parada, salva o peso dos pacotes carregadas na parada
            peso_excedente.append(peso_exc) #quando terminar a parada, salva o peso excedente carregado na parada
            print('Parada encerrada!') #encerra a parada
            break
    
    return peso_pacotes, quantidade_pacotes, peso_parada, peso_excedente, valor_excedente

def consulta_situacao(peso_max,capacidade_max,peso_pacotes,valor_pacotes):
    if (peso_pacotes == []) or (capacidade_max == []):
        print('Caminhão vazio!')
    else:
        print('Peso carregado:', sum(peso_pacotes), 'kg')

        peso_restante = peso_max - sum(peso_pacotes) #calcula o peso que sobra no caminhão
        print('Peso restante:',peso_restante,'kg')

        print('Peso máximo:',peso_max,'kg')
        print('Quantidade de pacotes carregados:', len(peso_pacotes))

        pacotes_restantes  = capacidade_max - len(peso_pacotes)
        print('Quantidade de pacotes restante:', pacotes_restantes)
        print('Quantidade máxima:', capacidade_max)
        print('Valor transportado R$', sum(valor_pacotes))
        print('Valor restante ou excedente: ')
        print('Valor padrão máximo: ')
        
        
def listar_pacotes(capacidade_max,peso_pacotes):
    
    if (peso_pacotes == []) or (capacidade_max == []):
        print('Caminhão vazio!')
        print('  ----\n/ |   |',end='')
        print('  | | | | | | ',end='') 
        print(' \n------|',end='')
        print('--------------',end='')
        print('\n\-()--| /()\ ', end='')
        print(' /()()\ ')
        
    else:
        print('Caminhão com capacidade de', capacidade_max, 'm³ com', len(peso_pacotes), 'pacote(s) carregado(s)')
    
        #imprime o desenho do caminhão na tela com os pacotes
        print('  ----\n/ |   |',end='')
        for i in range(0,capacidade_max):
            if i > len(peso_pacotes)-1:
                print(' | ',end='') 
            else:
                print('', peso_pacotes[i],'|',end='')      
        print(' \n------|',end='')
        for i in range(0,capacidade_max):
            print('------',end='')
        print('\n\-()--| /()\ ', end='')
        for i in range(0,capacidade_max):
            print('  ', end='')
        print(' /()()\ ')
        
print('1. Iniciar dia \n2. Realizar parada\n3. Consultar situação\n4. Listar pacotes\n'
      '5. Finalizar dia\n6. Gerar relatório\n7. Sair')  #Imprime as opções na 

#inicia os vetores como vazio
peso_pacotes = []
valor_pacotes = []
quantidade_pacotes = []
peso_parada = []
peso_excedente = []
opcoes = []
valor_excedente = []

while True:
    
    op = int(input('\nEscolha a opção desejada: ')) #Pede para o usuário escolher uma opção
    
    if op == 1:
        #limpa as variáveis
        peso_pacotes = []
        valor_pacotes = []
        quantidade_pacotes = []
        peso_parada = []
        peso_excedente = []
        opcoes= []
        valor_excedente = []
        
        opcoes.append(op) #salva todas as opções escolhidas
        #Pede para o usuário as informações de capacidades máximas
        capacidade_max = int(input('Digite o volume de carga do caminhão em metros cúbicos: '))
        peso_max = float(input('Digite o peso máximo de carga total em kg: ')) #
    elif op == 2:
        if 1 not in opcoes: #verifica se o valor 1 existe no vetor de opções escolhidas (verifica se o dia foi iniciado)
            print('O dia ainda não foi iniciado!') #se o dia ainda não tiver sido iniciado, exibe essa mensagem
        else:
            opcoes.append(op) #salva todas as opções escolhidas
            custo = 1.5 #custo de transporte = R$ 1.50 por kg
            print('a. Inserir pacote \nb. Retirar pacote \nc. Encerrar parada')           
            peso_pacotes, quantidade_pacotes, peso_parada, peso_excedente, valor_excedente = parada(peso_max,peso_pacotes,quantidade_pacotes,peso_parada,peso_excedente, valor_excedente)
    elif op == 3:
        if 1 not in opcoes: #verifica se o valor 1 existe no vetor de opções escolhidas (verifica se o dia foi iniciado)
            print('O dia ainda não foi iniciado!') #se o dia ainda não tiver sido iniciado, exibe essa mensagem
        else:
            opcoes.append(op) #salva todas as opções escolhidas
            consulta_situacao(peso_max,capacidade_max,peso_pacotes,valor_pacotes)
    elif op == 4:
        if 1 not in opcoes: #verifica se o valor 1 existe no vetor de opções escolhidas (verifica se o dia foi iniciado)
            listar_pacotes([],[])
        else:
            opcoes.append(op) #salva todas as opções escolhidas
            listar_pacotes(capacidade_max,peso_pacotes)
    elif op == 5:
        if 1 not in opcoes: #verifica se o valor 1 existe no vetor de opções escolhidas (verifica se o dia foi iniciado)
            print('O dia ainda não foi iniciado!') #se o dia ainda não tiver sido iniciado, exibe essa mensagem
        else:
            opcoes.append(op) #salva todas as opções escolhidas
            print('Encerrando as movimentações!')
    elif op == 6:
        if 5 not in opcoes: #verifica se o valor 5 existe no vetor de opções escolhidas (verifica que as movimentações foram encerradas)
            print('As movimentações ainda não foram encerradas!') #se as movimentações não tiverem sido encerradas, exibe essa mensagem
        else:
            gera_relatorio(peso_pacotes,valor_pacotes,quantidade_pacotes,peso_parada,peso_excedente,valor_excedente)
    elif op == 7:
        #Encerra o programa
        break
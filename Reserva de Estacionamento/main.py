import os

def gerador_estacionamento(nlinhas,ncolunas):
    matriz = [ [None]*ncolunas for i in range(nlinhas) ]

    for i in range (nlinhas):
        for j in range (ncolunas):
            matriz[i][j] = ['L', None, None]

    return matriz

def exibir_estacionamento(matriz):
    nlinhas = len(matriz)
    ncolunas = len(matriz[0])
    # Cria uma lista de letras do alfabeto (A-Z) para as colunas
    alfabeto = [chr(ord('A') + i) for i in range(ncolunas)]
    
    # Imprime o cabeçalho das colunas
    print('   ' + ' '.join([f'{letra:3}' for letra in alfabeto]))
    
    # Imprime as linhas com números e os valores da matriz
    for i in range(nlinhas):
        # Imprime o número da linha
        print(f'{i + 1:2} ', end='')
        # Imprime os valores da linha
        for j in range(ncolunas):
            print(f'{matriz[i][j][0]:4}', end='')
        print()
    
def consultar_posicao(matriz, posicao):
    # Solicita a posição ao usuário
    nlinhas = len(matriz)
    ncolunas = len(matriz[0])

    linha, letra = posicao.split('-')
    linha = int(linha) - 1
    coluna = ord(letra.upper()) - ord('A')
    
    if linha < 0 or linha >= nlinhas or coluna < 0 or coluna >= ncolunas:
        print("Posição fora dos limites da matriz.")
    else:
        valor = matriz[linha][coluna]
        return [valor[1], valor[2]]

def adicionar_carro(matriz, nome, placa, posicao):
    nlinhas = len(matriz)
    ncolunas = len(matriz[0])
    global estacionamento

    linha, letra = posicao.split('-')
    linha = int(linha) - 1
    coluna = ord(letra.upper()) - ord('A')
    
    if linha < 0 or linha >= nlinhas or coluna < 0 or coluna >= ncolunas:
        print("Posição fora dos limites da matriz.")
    else:   
        for i in range (nlinhas):
            for j in range (ncolunas):
                if i == linha and j == coluna:
                    estacionamento[i][j] = ['O', nome, placa]

def remover_carro(matriz, posicao):
    nlinhas = len(matriz)
    ncolunas = len(matriz[0])
    global estacionamento

    linha, letra = posicao.split('-')
    linha = int(linha) - 1
    coluna = ord(letra.upper()) - ord('A')
    
    if linha < 0 or linha >= nlinhas or coluna < 0 or coluna >= ncolunas:
        print("Posição fora dos limites da matriz.")
    else:   
        for i in range (nlinhas):
            for j in range (ncolunas):
                if i == linha and j == coluna:
                    estacionamento[i][j] = ['L', None, None]

estacionamento = gerador_estacionamento(3, 3)

# Main
while True:
    print('''
    Sistema de Estacionamento
          
    A - Ver Mapa do Estacionamento
    B - Verificar Carro em Vaga
    C - Adicionar Carro em Vaga
    D - Remover Carro
    E - Sair
    ''')
    opcao = input('Escolha uma opção: ').lower()
    os.system('cls')

    if opcao == 'a':
        exibir_estacionamento(estacionamento)
        input('Pressione ENTER pra continuar')
        os.system('cls')

    elif opcao == 'b':
        exibir_estacionamento(estacionamento)
        linha = input('Me diga a Linha em que seu carro está posicionado: ').strip()
        coluna = input('Me diga a Letra em que seu carro está posicionado: ').strip()
        posicao = linha + '-' + coluna
        carro = consultar_posicao(estacionamento, posicao)
        print(carro)
        input('Pressione ENTER pra continuar')
        os.system('cls')

    elif opcao == 'c':
        exibir_estacionamento(estacionamento)
        linha = input('Me diga a Linha em que seu carro está posicionado: ').strip()
        coluna = input('Me diga a Letra em que seu carro está posicionado: ').strip()
        posicao = linha + '-' + coluna

        nome = input('Qual o nome do Motorista? ')
        placa = input('Qual a placa do carro? ')
        adicionar_carro(estacionamento, nome, placa, posicao)

        print('Carro adicionado com sucesso 👍')
        input('Pressione ENTER pra continuar')
        os.system('cls')

    elif opcao == 'd':
        exibir_estacionamento(estacionamento)
        linha = input('Me diga a Linha em que seu carro está posicionado: ').strip()
        coluna = input('Me diga a Letra em que seu carro está posicionado: ').strip()
        posicao = linha + '-' + coluna

        remover_carro(estacionamento, posicao)
        print('Carro removido com sucesso 👍')
        input('Pressione ENTER pra continuar')
        os.system('cls')

    elif opcao == 'e':
        print('Muito obrigado por usar nosso sistema 😊')
        break

    else: 
        print("Digite uma opção válida")
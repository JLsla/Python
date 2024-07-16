# 4. Faça um programa que leia duas matrizes de inteiros e gere uma terceira matriz que corresponderá a soma das duas matrizes lidas. A ordem das matrizes também será lida.
# O programa deverá conter as seguintes funções:
#   • Uma função para gerar e ler uma matriz, sendo passados como parâmetros a ordem da matriz.
#   • Uma função para exibir uma matriz em sua representação clássica (linhas e colunas).
#   • Uma função para somar duas matrizes.
import random
def gerador_matriz(nlinhas,ncolunas):
    matriz = [ [None]*ncolunas for i in range(nlinhas) ]

    for i in range (nlinhas):
        for j in range (ncolunas):
            matriz[i][j] = random.randint(1,10)

    return matriz

def exibir_matriz(matriz,nlinhas,ncolunas):
    for i in range(nlinhas):
        for j in range(ncolunas):
            print(f'{matriz[i][j]:4}', end='')
        print()

def soma_matriz(nlinhas, ncolunas, Amatriz, Bmatriz):
    matriz = gerador_matriz(nlinhas,ncolunas)
    for i in range (nlinhas):
        for j in range (ncolunas):
            matriz[i][j] = Amatriz[i][j] + Bmatriz[i][j]
    return matriz

nlinhas = 3
ncolunas = 3
Amatriz = gerador_matriz(nlinhas,ncolunas)
Bmatriz = gerador_matriz(nlinhas,ncolunas)
Cmatriz = soma_matriz(nlinhas,ncolunas, Amatriz, Bmatriz)
exibir_matriz(Amatriz, nlinhas, ncolunas)
print()
exibir_matriz(Bmatriz, nlinhas, ncolunas)
print()
exibir_matriz(Cmatriz, nlinhas, ncolunas)
# 1. Escreva um programa que preencha duas matrizes (A e B), ambas de ordem 2x3, com valores inteiros fornecidos pelo usuário (ou gerados aleatoriamente). O programa deverá somar as duas matrizes, armazenando o resultado em uma terceira matriz (C). Ao final, exiba as 3 matrizes (no formato de matriz).

import random

nlinhas = 2
ncolunas = 3
Amatriz = [ [None]*ncolunas for i in range(nlinhas) ]
Bmatriz = [ [None]*ncolunas for i in range(nlinhas) ]

for i in range (nlinhas):
    for j in range (ncolunas):
        Amatriz[i][j] = random.randint(1,10)
        Bmatriz[i][j] = random.randint(1,10)

Cmatriz = [ [None]*ncolunas for i in range (nlinhas)]

for i in range (nlinhas):
    for j in range (ncolunas):
        Cmatriz[i][j] = Amatriz[i][j] + Bmatriz[i][j]
    

for i in range(nlinhas):
    for j in range(ncolunas):
        print(f'{Amatriz[i][j]:4}', end='')
    print()

print ()

for i in range(nlinhas):
    for j in range(ncolunas):
        print(f'{Bmatriz[i][j]:4}', end='')
    print()
 
print ()

for i in range(nlinhas):
    for j in range(ncolunas):
        print(f'{Cmatriz[i][j]:4}', end='')
    print()


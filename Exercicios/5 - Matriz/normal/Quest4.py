#  4. Uma matriz transposta é a matriz que se obtém da troca de linhas por colunas de uma dada matriz. Assim, dada uma matriz C de ordem m x n, a matriz transposta dela será representada por Ct de ordem n x m, onde cada elemento de Ct[i,j] = C[j,i]. Escreva um programa que preencha uma matriz 3x5 com valores inteiros fornecidos pelo usuário (ou gerados aleatoriamente) e gere a sua transposta. Ao final, imprima as duas matrizes (no formato de matriz).

import random

nlinhas = 3
ncolunas = 5  
a = [[None]*ncolunas for i in range (nlinhas)]
at = []

for i in range (nlinhas):
    for j in range (ncolunas):
        a[i][j] = random.randint(0,9)

for i in range(ncolunas):
    linhat = []
    for j in range(nlinhas):
        if (j > nlinhas-1):
            break
        linhat.append(a[j][i])
    at.append(linhat)

for i in range (nlinhas):
    for j in range (ncolunas):
        print(f'{a[i][j]:4}', end='')        
    print()

print()

for i in range (ncolunas):
    for j in range (nlinhas):
        print(f'{at[i][j]:4}', end='')        
    print()
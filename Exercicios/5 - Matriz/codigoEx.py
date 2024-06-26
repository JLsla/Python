nlinhas = 2 # Quantidade de Linhas da Matriz
ncolunas = 3 # Quantidade de Colunas da Matriz

matriz = [ [None]*ncolunas for i in range(nlinhas) ] # Criando a Matriz

# Acessando cada posição da Matriz
for i in range(nlinhas):
    for j in range(ncolunas):
        matriz[i][j] = int(input(f'Matriz[{i}][{j}]: '))

# Printando a Matriz como uma Matriz, não como uma Lista de Listas 
for i in range(nlinhas):
    for j in range(ncolunas):
        print(f'{matriz[i][j]:4}', end='')
    print()
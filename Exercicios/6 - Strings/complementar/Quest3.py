# 3. Faça um programa que leia o nome de uma pessoa e exiba-o conforme o exemplo abaixo.
# Obs: Suponha que o nome lido não possua nenhuma preposição, artigo, etc.
# Exemplo:  Entrada: FLAVIO RIBEIRO COUTINHO
#           Saída: COUTINHO, F. R.

nome = input("Informe seu nome:  ").upper()
nome = nome.split()
formatado = []
formatado.append(nome[-1])
del(nome[-1])

for i in nome:
    formatado.append(i[0])

for i in range(len(formatado)):
    if i == 0:
        print(f'{formatado[i]}', end=', ')
    else:    
        print(f'{formatado[i]}', end='. ')
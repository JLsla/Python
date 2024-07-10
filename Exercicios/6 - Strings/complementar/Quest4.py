# 4. Faça um programa que leia uma string S e um valor inteiro N, e exiba na tela a string S com as suas vogais repetidas N vezes.
#Exemplo:
#Entrada: S: Hoje tem aula de Python

#N: 3

#Saída: Hooojeee teeem aaauuulaaa deee Pythooon

frase = 'Hoje tem aula de Python'
frase = frase.split()
n = 3

for i in range(len(frase)):
    letras = []
    palavra = ''

    for j in range(len(frase[i])):
        letras.append(frase[i][j])
    
    for j in range(len(letras)):
        if letras[j] in 'aeiouAEIOU':
            letras[j] = letras[j] * n
            palavra += letras[j]
        else:
            palavra += letras[j]
        
    frase[i] = palavra

for i in frase:
    print(f'{i} ', end='')
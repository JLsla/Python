#3. Escreva uma função chamada vertical que receba como parâmetro uma string e a exiba na vertical, ou seja, com uma letra em cada linha. Faça também um programa para testar a função.

def vertical (palavra):
    for letra in palavra:
        print(letra)
vertical ("palavra")
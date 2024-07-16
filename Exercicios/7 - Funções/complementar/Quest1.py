# 1. Escreva uma função chamada vogal que receba uma letra e verifique se a letra é uma vogal, retornando o valor True nesse caso, ou o valor False caso contrário. Escreva também um programa que leia uma frase e, usando a função vogal criada, imprima a quantidade de vogais existentes na frase lida.

def verificaVogal(letra):
    if letra in 'aeiouAEIOU':
        return True
    else:
        return False

frase = 'Me diga uma frase'

quatVogais = 0
for letra in frase:
    if verificaVogal(letra):
        quatVogais += 1
    else:
        continue
print(quatVogais)
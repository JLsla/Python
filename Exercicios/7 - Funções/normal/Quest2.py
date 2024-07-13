# 2. Escreva uma função chamada fatorial que receba um número inteiro e retorne seu fatorial. Faça também um programa para testar a função.

def fatorial (num1):
    mult = 1

    fatorial = f"{num1}! = 1"
    if num1 == 0:
        return fatorial
    for i in range (1, num1+1, 1):
        if i == 1:
            continue
        fatorial = fatorial + f' x {i}'
        mult *= i

    return fatorial + ' = ' + f'{mult}'
       
print(fatorial(3))

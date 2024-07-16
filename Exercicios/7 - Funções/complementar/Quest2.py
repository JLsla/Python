# 2. Escreva uma função chamada primo para determinar se um número é primo ou não. A função deve receber um número inteiro, retornar True se o número for primo, ou False caso contrário. Escreva também um programa que, usando a função primo criada, exiba os números primos entre 1 e 100.

def verificaPrimo(numero):
    resto_divisao = 0

    for num in range (1, numero + 1, 1):
        if (numero % num == 0):
            resto_divisao+=1
            
    if (resto_divisao == 2):
        return True
    else:
        return False
    
i = 1
primos = 0
nao_primos = 0

while i < 101:
    if verificaPrimo(i):
        primos += 1
    else:
        nao_primos += 1    
    i += 1

print(f'A quantidade de números primos é: {primos}')
print(f'A quantidade de números não primos é: {nao_primos}')
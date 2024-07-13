# 1. Escreva uma função chamada menor que receba 3 números e retorne o menor deles. Faça também um programa para testar a função.

def menor (num1, num2, num3):
    if num1 < num2 and num1 < num3:
         return num1
    elif num2 < num1 and num2 < num3:
         return num2
    elif num3 < num2 and num3 < num1:
         return num3
    
menor = menor(23, 2, 33)
print(menor)
# 8. Faça um programa que leia um número inteiro N, calcule e mostre o maior quadrado perfeito menor ou igual a N. Por exemplo, se N for igual a 38, o resultado é 36.
import math

num1 = int(input("Digite um número: "))

sla = 0

for num in range (num1, 0, -1):
    quadrado = math.sqrt(num)
    if quadrado.is_integer():
        sla =+ num
        break
    
print(f"{sla} é o maior quadrado perfeito de {num1} ")
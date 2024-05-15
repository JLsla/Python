# 5. Escreva um programa para determinar as raízes de uma equação de segundo grau, dados os seus coeficientes. Fórmulas: 
# Obs: se Δ for negativo, não existem as raízes da equação.
# Dica: use a função sqrt do módulo math.

import math

a = int(input("Digite o representante do A: "))
b = int(input("Digite o representante do B: "))
c = int(input("Digite o representante do C: "))

delta = (b ** 2) - (4 * a * c)

if (delta < 0):
    print(f"{delta} não tem raiz")

else:
    x1 = - (b) + math.sqrt(delta) /2 * (a)
    x2 = - (b) - math.sqrt(delta) /2 * (a) 
    print(f"a raiz de  {a}X² + {b}X + {c} são x1 = {x1} e x2 = {x2}")     
# math.sqrt(delta)
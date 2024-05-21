# 1. Faça um programa que calcule e mostre os números múltiplos de 5 do intervalo 50 a 300, juntamente com suas raízes e seus cubos.

import math

for i in range (50, 301, 1):
    print((i * 5))
    print(math.sqrt(i))
    print((i * i) * i)
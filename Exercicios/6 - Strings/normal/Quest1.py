# 1. Faça um programa que leia uma frase e determine a quantidade de brancos contidos na mesma.

frase = input("Diga uma frase; ")
contador = 0
tamanho = len (frase)
for i in range (tamanho):
    if frase[i] == " ":
        contador += 1
print(contador)
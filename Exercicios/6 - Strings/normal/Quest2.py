# 2. Faça um programa que leia uma frase e a exiba sem os espaços em branco.

frase = input("Diga uma frase; ")
divisao = frase.split()
frase2 = "" 
for i in divisao:
    frase2 += i
print(frase2)
# 4. Escreva um programa para ler 6 números distintos, ou seja, não podem repetir. Exiba os números lidos.

n = 6
v = [None]*n

repitido = False
flag=0
while flag < n:
    a = int(input("Digite um número equivalente a os números do vetor: "))
    for j in range (flag):
        if a == v[j]:
            print(f"esse número ja existe, favor escrever outro")
            repitido = True
            break
    if repitido == True:
        repitido = False 
        continue
    v[flag] = a  
    flag += 1
print(v)
# 3. Escreva um programa que solicite a digitação de um ano e imprima sua classificação como bissexto ou não bissexto. Obs: um ano é bissexto se for divisível por 4, mas não por 100. Um ano também é bissexto se for divisível por 400.               
ano = int(input("Digite um ano: "))

if ((ano % 4 == 0)):
    print(f"{ano} é um ano bissexto")
    
elif ((ano % 4 != 0)):
    print(f"{ano} não é um ano bissexto")

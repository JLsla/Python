# 2. Escreva um programa que solicite a digitação de um caractere qualquer do teclado e imprima sua classificação: vogal, consoante, número e caractere especial.

caracter = input("Digite um caractere qualquer, do seu terclado: ")

cod_caracter = ord(f"{caracter}")

if (cod_caracter >=48 and cod_caracter <=57):
    print(f"{caracter} é um número")

elif ((cod_caracter >=33 and cod_caracter <=47 )or(cod_caracter >=58 and cod_caracter <=64 )or(cod_caracter >=91 and cod_caracter <=96 )or(cod_caracter >=123 and cod_caracter <=126 )):
    print(f"{caracter} é um caracter especial")

elif ((cod_caracter >=66 and cod_caracter <=68 )or(cod_caracter >=70 and cod_caracter <=72 )or(cod_caracter >=74 and cod_caracter <=78 )or(cod_caracter >=80 and cod_caracter <=84 )or(cod_caracter >=86 and cod_caracter <=90 )or(cod_caracter >=98 and cod_caracter <=100 )or(cod_caracter >=102 and cod_caracter <=104 )or(cod_caracter >=106 and cod_caracter <=110 )or(cod_caracter >=112 and cod_caracter <=116 )or(cod_caracter >=118 and cod_caracter <=122 )):
    print(f"{caracter} é uma consoante")

elif ((cod_caracter == 65) or (cod_caracter == 69) or (cod_caracter == 73) or (cod_caracter == 79) or (cod_caracter == 85) or (cod_caracter == 97)or(cod_caracter == 101)or(cod_caracter == 105)or(cod_caracter == 111)or (cod_caracter == 117)):
    print(f"{caracter} é uma vogal")
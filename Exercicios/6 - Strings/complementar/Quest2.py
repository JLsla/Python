# 2. Faça um programa que leia uma frase e a exiba criptografada. O método de criptografia será baseado na seguinte regra: trocar alguns caracteres por outros, conforme a tabela abaixo:
frase = input("Diga uma frase; ").lower()
frase_codificada = []
for i in frase:
    if i == " ":
        frase_codificada.append ("a")
    elif i == "e":
        frase_codificada.append ("u")
    elif i == "i":
        frase_codificada.append ("o")
    elif i == "o":
        frase_codificada.append ("i")
    elif i == "u":
        frase_codificada.append ("e")
    elif i == "a":
        frase_codificada.append (" ")
    else:
        frase_codificada.append (i)
for i in frase_codificada:
    print(f"{i}", end = "") 
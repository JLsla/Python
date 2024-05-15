# 7. Escreva um programa que leia o peso (kg) e a altura (m) de uma pessoa, determine e mostre o seu grau de obesidade, de acordo com a tabela seguinte. O grau de obesidade é determinado pelo índice de massa corpórea, cujo cálculo é realizado dividindo-se o peso da pessoa pelo quadrado da sua altura.                                                        < 26 = Normal \\  > 26 e < 30 Obeso \\ > 30 Obeso mórbido

peso = int(input("Quanto essa pessoa pesa em (kg): "))
altura = int(input("Qual a alturadessa pessoa em (m): "))

imc = peso / (altura ** 2)

if imc <= 26:
    print(f"Essa pessoa está normal")

elif imc == 26 or imc <= 30:
    print(f"Essa pessoa está obesa")

else:
    print(f"Essa pessoa está com obesidade mórbida")
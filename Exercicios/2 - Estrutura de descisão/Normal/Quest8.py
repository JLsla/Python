# 8. Escreva um programa que tenha a funcionalidade de uma calculadora simples. O programa deve solicitar a digitação de dois operandos e um operador (+ - x * / %) e deve imprimir ao resultado da operação aritmética. Caso o usuário digite um operador inválido, o programa deve imprimir "Operador desconhecido".

num1= float(input("Qual o primeiro número para começar a conta: "))
num2= float(input("Qual o segundo número: "))
operador= input("Qual a conta para finalizar a conta: ")

if (operador == "+"):
   soma = num1 + num2
    print(f"{num1} + {num2} = a {soma} ")

elif (operador == "-"):
    subtracao = num1 - num2
    print(f"A subtração de {num1} com {num2} é igual a {subtracao}")
        
elif (operador == "x" or operador == "."):
   multiplicacao = num1 * num2
    print(f"A multiplicação entre {num1} e {num2} é igual a {multiplicacao}")

elif (operador == "*"):
potenciacao = num1 ** num2
    print(f"A potenciação de {num1} com {num2} é igual a {potenciacao}")

elif (operador == "/"):
    divisao = num1 / num2
    print(f"Adivisão entre {num1} e {num2} é igual a {divisao}")

elif (operador == "%"):
    porcentagem = num1
    print(f"A porcentagem de {num1} sobre {num2} é igual a {porcentagem}")

else:
    print(f"digite dois números existentes e um operador existente Ex: +, -, x, *, / ou %")
# 8. O cardápio de uma casa de lanches, especializada em sanduíches, é dado a seguir.
# CÓDIGO NOME PREÇO
# H Hamburger R$ 5,00
# C Cheese Burger R$ 6,00
# B Cheese Bacon R$ 7,00
# F Cheese Frango R$ 4,00

# Faça um programa que leia o código e a quantidade de cada item comprado por um cliente (a leitura do código “X” indica o fim dos dados de entrada). Ao final, calcule e exiba o total a pagar.
# Veja o exemplo abaixo, considerando que o cliente pediu 3 Hamburger e 2
# Cheese Bacon:
# Entrada:
# Código: H
# Quantidade: 3
# Código: B
# Quantidade: 2
# Código: X
# Saída:
# Total a pagar: R$ 29.00

total = 0.0
h = 5.00
c= 6.00
b = 7.00
f = 4.00
finalizar = 0

while finalizar == "x":
    h = int(input("Hamburguer: "))
    finalizar = input(f"Para finalizar digitar x ou X").lower()
    c = int(input("Cheese Burguer: "))
    finalizar = input(f"Para finalizar digitar x ou X").lower()
    b = int(input("Cheese Bacon: "))
    finalizar = input(f"Para finalizar digitar x ou X").lower()
    f = int(input("Cheese Frango: "))
   
    



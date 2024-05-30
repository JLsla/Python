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

while True:
    codigo = input('Qual o código do seu pedido? ').lower()
    if codigo == 'x':
        break
    else:
        quant = int(input("Qual a quantidade? "))
        if (codigo == 'h'):
            total += (quant * h)
        elif codigo == 'c':
            total += (quant * c)
        elif codigo == 'b':
            total += (quant * b)
        elif codigo == 'f':
            total += (quant * f)
        else:
            print('Digite um código válido!')
            
print(f'O total da sua compra deu {total}')
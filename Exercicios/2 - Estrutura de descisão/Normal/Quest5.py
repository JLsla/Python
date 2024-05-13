# A empresa Vende Tudo Ltda paga o salário de cada vendedor com uma comissão de 5% sobre o total de vendas daquele vendedor, mas essa comissão nunca deve ser inferior ao salário- mínimo. Escreva um programa que leia o valor total das vendas de um vendedor e escreva seu salário.

total_vendas = int(input("Quantas vendas ele fez: "))
comissao = total_vendas * 0.05
if (comissao < 1.412):
    print(f"Salário do vendedor é de {comissao}")
else:
    print(f"O funcionário não atingiu o salário mínimo")
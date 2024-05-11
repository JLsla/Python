# 1. A Companhia de Carros Usados João Honesto paga seus empregados um salário de R$ 1.000,00 por mês mais uma comissão de R$ 200,00 por cada carro vendido mais 5% do valor da venda.                             Escreva um programa que leia o nome, o número de carros vendidos e o valor total das vendas de um vendedor, e calcule e exiba o seu salário.

nome = input('Qual seria o nome do funcionário? ')

carro_vendido = int(input(f'Quantos carros {nome} vendeu? '))

valor_venda = float(input('Qual o valor da venda de todos os carros vendido? '))

salario_mensal = 1000 #Salário mensal do funcionário

comissao_por_carro = 200 #Comissão por venda de carro

porcentagem_valor_venda = 0.05 * valor_venda #5% do valor da venda total

salario_total = salario_mensal + (carro_vendido*comissao_por_carro) + porcentagem_valor_venda

print(f'o salário total de {nome} é de {salario_total:.2f} ')
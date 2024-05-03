# 6. Faça um programa que efetue a apresentação do valor da conversão em real (R$) de um valor lido em dólar (US$). O algoritmo deverá solicitar o valor da cotação do dólar e também a quantidade de dólares disponíveis com o usuário.

dolar = float(input('Quantos dólares você tem? '))
cotacao = float(input('Qual seria a cotação?'))
multiplicacao = dolar*cotacao
print(f"você tem {multiplicacao} reais")
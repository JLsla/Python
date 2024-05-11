# 2. Escreva um programa para calcular e exibir a média ponderada de 2 notas dadas. Sabe-se que nota1 possui peso 6 e nota2 possui peso 4.

nota1 = int(input('nota: '))
nota2 = int(input('nota: '))
nota3 = int(input('nota: '))

soma = (nota1 * 1) + (nota2 * 2) + (nota3 * 3)
resultado = soma // (1+2+3)

print(f'O resultado é {resultado}')
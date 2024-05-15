# 1. Escreva um programa que solicite a digitação de um número (de 1 a 7) correspondente a um dia da semana e imprima o nome do dia da semana e se é dia útil (de segunda a sexta) ou final de semana (sábado e domingo). Considere que o dia 1 é o domingo.

dia = int(input("digite um número equivalente ao dia da semana (considere domingo com dia 1): "))

if dia == 1:
    dia = "Domingo é Final de semana"
    print(dia)
     
elif dia == 2:
    dia = "Segunda-feira é Dia útil"
    print(dia)
    
elif dia == 3:
    dia = "Terça-feira é Dia útil"
    print(dia)
    
elif dia == 4:
    dia = "Quarta-feira é Dia útil"
    print(dia)
    
elif dia == 5:
    dia = "Quinta-feira é Dia útil"
    print(dia)
    
elif dia == 6:
    dia = "Sexta-feira é Dia útil"
    print(dia)
   
elif dia == 7:
    dia = "Sábado é Final de semana"
    print(dia)
    
else:
    dia = "Número inválido"
    print(dia)
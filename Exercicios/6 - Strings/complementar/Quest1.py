# 1. Faça um programa que leia o email de uma pessoa e mostre, separadamente, qual o login e qual o domínio. Por exemplo, suponha que o email seja "fulano@provedor.com.br", então o login será "fulano" e o domínio será "provedor.com.br".

email = input("Diga seu email: ")
divisao = email.split("@")
dominio = divisao[1]
email = divisao[0]
print(f'seu email é {email} e seu dominio é {dominio}')
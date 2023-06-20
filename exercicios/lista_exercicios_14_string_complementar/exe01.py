"""
1. Faça um programa que leia o email de uma pessoa e mostre, separadamente,
qual o login e qual o domínio. Por exemplo: "fulano@provedor.com.br",
então o login será "fulano" e o domínio será "provedor.com.br".
"""
email = input('E-mail: ').split('@')

print(f'Login: {email[0]}\nProvedor: {email[1]}')

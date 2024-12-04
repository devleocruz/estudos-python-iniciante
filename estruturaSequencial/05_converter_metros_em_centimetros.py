"""
Faça um Programa que converta metros para centímetros.
"""
try:
    metro = float(input("Digite o numero em metros:\n"))

    centimetro = metro * 100 # 1 metro = 100 centímetros

    print(f"{metro:.2f} metro(s) é igual a {centimetro:.2f} centimetro(s)")
    
except ValueError:
    print("Erro: Você digitou um número inválido!")
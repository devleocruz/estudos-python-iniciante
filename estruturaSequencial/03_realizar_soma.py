"""
Faça um Programa que peça dois números e imprima a soma.
"""
try:
    # Entrada de dados
    numero_1 = float(input("Digite o primeiro número da soma:\n"))
    numero_2= float(input("Digite o segundo número da soma:\n"))

    # Processamento
    soma = numero_1 + numero_2

    # Saida
    print(f"{numero_1} + {numero_2} = {soma:.2f}")
    
except ValueError:
    print("Erro: Você digitou um número inválido!")
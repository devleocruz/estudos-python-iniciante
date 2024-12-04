"""
Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula:
(72.7*altura) - 58
"""
try:
    altura = float(input("Digite sua altura em metros:\n"))

    peso_ideal = (72.7 * altura) - 58

    print(f"Seu peso ideal é {peso_ideal:.2f} kg")

except ValueError:
    print("Erro: Você digitou um número inválido!")


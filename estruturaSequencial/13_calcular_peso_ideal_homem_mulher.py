"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
"""
try:
    altura = float(input("Digite a altura em metros:\n"))

    peso_ideal_homem = (72.7 * altura) - 58
    peso_ideal_mulher = (62.1 * altura) - 44.7

    print(f"Para homens com {altura:.2f} metros de altura o peso ideal é: {peso_ideal_homem:.2f} kg")
    print(f"Para mulheres com {altura:.2f} metros de altura o peso ideal é: {peso_ideal_mulher:.2f} kg")

except ValueError:
    print("Erro: Você digitou um número inválido!")

# Eu até pensei em fazer com if-elif-else, mas este não é um exercício de estrutura condicional e, sim, sequencial.
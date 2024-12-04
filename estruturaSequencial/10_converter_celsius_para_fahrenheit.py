"""
Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
"""
try:
    celsius = float(input("Digite a temperatura em graus Celsius:\n"))
    fahrenheit = (9 * celsius / 5) + 32

    print(f"{celsius:.2f}°C é {fahrenheit:.2f}°F")

except ValueError:
    print("Erro: Você digitou um número inválido!")
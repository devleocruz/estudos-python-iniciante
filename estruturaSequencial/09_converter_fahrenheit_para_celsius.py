"""
Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
 C = 5 * ((F-32) / 9).
"""
try:
    temperatura_fahrenheit = float(input("Digite a temperatura em graus Fahrenheit:\n"))

    temperatura_celsius = 5 * ((temperatura_fahrenheit - 32) / 9)

    print(f"{temperatura_fahrenheit:.2f}°F é {temperatura_celsius:.2f}°C")
    
except ValueError:
    print("Erro: Você digitou um número inválido!")
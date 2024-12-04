"""
Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
"""
import math # Biblioteca do Python usada para realizar cálculos matemáticos.
try:
    raio = float(input("Digite o raio do circulo:\n"))

    area = math.pi * (raio ** 2) # A fórmula para a área de um círculo é 𝐴=𝜋×𝑟^2

    print(f"A area é {area:.2f}")
     
except ValueError:
    print("Erro: Você digitou um número inválido!")